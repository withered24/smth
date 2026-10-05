/* Al Rayan Rings — small behaviours for the ar-* sections. Safe to load more than once. */
(function () {
  if (window.__arRayan) { window.__arRayan.init(); return; }
  document.documentElement.classList.add('ar-js');

  function formatMoney(cents, format) {
    format = format || '${{amount}}';
    var v = (cents / 100);
    function withSep(n, dec, thou, decSep) {
      var parts = n.toFixed(dec).split('.');
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, thou);
      return parts.join(decSep);
    }
    return format.replace(/\{\{\s*(\w+)\s*\}\}/, function (_, key) {
      switch (key) {
        case 'amount_no_decimals': return withSep(v, 0, ',', '.');
        case 'amount_with_comma_separator': return withSep(v, 2, '.', ',');
        case 'amount_no_decimals_with_comma_separator': return withSep(v, 0, '.', ',');
        default: return withSep(v, 2, ',', '.');
      }
    });
  }

  function reveal(root) {
    var els = root.querySelectorAll('[data-ar-reveal]:not(.is-in)');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('is-in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (e) { io.observe(e); });
  }

  function gallery(el) {
    if (el.dataset.arInit) return; el.dataset.arInit = '1';
    var main = el.querySelector('[data-ar-main]');
    var thumbs = Array.prototype.slice.call(el.querySelectorAll('[data-ar-thumb]'));
    var i = 0;
    function show(n) {
      if (!thumbs.length) return;
      i = (n + thumbs.length) % thumbs.length;
      var t = thumbs[i];
      main.src = t.dataset.src; main.srcset = t.dataset.srcset || ''; main.alt = t.dataset.alt || '';
      thumbs.forEach(function (b, k) { b.setAttribute('aria-current', k === i ? 'true' : 'false'); });
    }
    thumbs.forEach(function (b, k) { b.addEventListener('click', function () { show(k); }); });
    var prev = el.querySelector('[data-ar-prev]'), next = el.querySelector('[data-ar-next]');
    if (prev) prev.addEventListener('click', function () { show(i - 1); });
    if (next) next.addEventListener('click', function () { show(i + 1); });
    el.arShowMedia = function (id) {
      thumbs.forEach(function (b, k) { if (String(b.dataset.mediaId) === String(id)) show(k); });
    };
  }

  function product(el) {
    if (el.dataset.arInit) return; el.dataset.arInit = '1';
    var dataEl = el.querySelector('[data-ar-variants]');
    if (!dataEl) return;
    var variants = JSON.parse(dataEl.textContent);
    var fmt = el.dataset.moneyFormat;
    var idInput = el.querySelector('[data-ar-variant-id]');
    var groups = Array.prototype.slice.call(el.querySelectorAll('[data-ar-option]'));
    var gal = el.querySelector('[data-ar-gallery]');

    function selected() {
      return groups.map(function (g) {
        var c = g.querySelector('input:checked') || g.querySelector('input[type=hidden]');
        return c ? c.value : null;
      });
    }
    function find(vals) {
      return variants.find(function (v) { return v.options.every(function (o, k) { return vals[k] === null || o === vals[k]; }); });
    }
    function update() {
      var vals = selected();
      var v = find(vals);
      groups.forEach(function (g, k) {
        var label = g.querySelector('[data-ar-selected]');
        if (label) label.textContent = vals[k] || '';
        g.querySelectorAll('input[type=radio]').forEach(function (inp) {
          var test = vals.slice(); test[k] = inp.value;
          var m = find(test);
          inp.nextElementSibling.classList.toggle('is-unavailable', !m || !m.available);
        });
      });
      var btns = document.querySelectorAll('[data-ar-atc="' + el.id + '"]');
      if (!v) {
        btns.forEach(function (b) { b.disabled = true; b.querySelector('[data-ar-atc-label]').textContent = b.dataset.unavailable; });
        return;
      }
      idInput.value = v.id;
      document.querySelectorAll('[data-ar-price="' + el.id + '"]').forEach(function (p) { p.textContent = formatMoney(v.price, fmt); });
      document.querySelectorAll('[data-ar-was="' + el.id + '"]').forEach(function (p) {
        var on = v.compare_at_price && v.compare_at_price > v.price;
        p.hidden = !on; if (on) p.textContent = formatMoney(v.compare_at_price, fmt);
      });
      document.querySelectorAll('[data-ar-save="' + el.id + '"]').forEach(function (p) {
        var on = v.compare_at_price && v.compare_at_price > v.price;
        p.hidden = !on; if (on) p.textContent = p.dataset.template.replace('[amount]', formatMoney(v.compare_at_price - v.price, fmt));
      });
      var visible = groups.filter(function (g) { return !g.hidden; }).map(function (g) { return vals[groups.indexOf(g)]; });
      document.querySelectorAll('[data-ar-variant-title="' + el.id + '"]').forEach(function (p) { p.textContent = visible.join(' / '); });
      btns.forEach(function (b) {
        b.disabled = !v.available;
        b.querySelector('[data-ar-atc-label]').textContent = v.available ? b.dataset.available : b.dataset.soldout;
      });
      if (v.featured_media && gal && gal.arShowMedia) gal.arShowMedia(v.featured_media.id);
      if (el.dataset.updateUrl === 'true' && window.history.replaceState) {
        var u = new URL(window.location.href); u.searchParams.set('variant', v.id);
        window.history.replaceState({}, '', u.toString());
      }
    }
    groups.forEach(function (g) { g.addEventListener('change', update); });
    if (gal) gallery(gal);
    update();
  }

  function dialogs(root) {
    root.querySelectorAll('[data-ar-open]').forEach(function (b) {
      if (b.dataset.arInit) return; b.dataset.arInit = '1';
      b.addEventListener('click', function () {
        var d = document.getElementById(b.dataset.arOpen);
        if (d && d.showModal) d.showModal();
      });
    });
    root.querySelectorAll('dialog.ar-dialog').forEach(function (d) {
      if (d.dataset.arInit) return; d.dataset.arInit = '1';
      d.addEventListener('click', function (e) { if (e.target === d || e.target.closest('[data-ar-close]')) d.close(); });
    });
  }

  function sticky(el) {
    if (el.dataset.arInit) return; el.dataset.arInit = '1';
    var trigger = document.getElementById(el.dataset.trigger);
    if (!trigger) return;
    var ticking = false;
    function check() {
      ticking = false;
      el.classList.toggle('is-visible', trigger.getBoundingClientRect().bottom < 0);
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(check); } }, { passive: true });
    check();
  }

  function init() {
    reveal(document);
    document.querySelectorAll('[data-ar-product]').forEach(product);
    document.querySelectorAll('[data-ar-gallery]').forEach(gallery);
    document.querySelectorAll('[data-ar-sticky]').forEach(sticky);
    dialogs(document);
  }

  window.__arRayan = { init: init, formatMoney: formatMoney };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  document.addEventListener('shopify:section:load', init);
})();
