"""Build report_v2.html (rewrite round) next to report.html so the same media paths work.

Run from anywhere:  python3 05-rewrite/build_report.py
Needs: pip install markdown
"""
import html
import re
from pathlib import Path

import markdown

RUN = Path(__file__).resolve().parent.parent
RW = RUN / "05-rewrite"
OUT = RUN / "report_v2.html"

ADS = [f"ad_{n:02d}" for n in range(1, 12)]
VIDEO = {"ad_06", "ad_07", "ad_08"}

# Re-render status per ad (from each final.md "Re-render needed"): (label, css class)
RERENDER = {
    "ad_01": ("Re-render optional", "ok"),
    "ad_02": ("Re-render required", "bad"),
    "ad_03": ("Re-render required", "bad"),
    "ad_04": ("Text re-render recommended", "mid"),
    "ad_05": ("Re-render required", "bad"),
    "ad_06": ("New VO + captions only", "ok"),
    "ad_07": ("New VO + captions + overlays", "ok"),
    "ad_08": ("New VO + captions + pill patches", "ok"),
    "ad_09": ("Text re-render optional", "ok"),
    "ad_10": ("Label re-render needed", "mid"),
    "ad_11": ("Text re-render needed", "mid"),
}


def md(text):
    return markdown.markdown(text, extensions=["tables", "sane_lists"])


def sections(text):
    """Split a markdown file into (heading, body) pairs on '## ' headings."""
    parts = re.split(r"^## +(.+)$", text, flags=re.M)
    head = parts[0]
    out = [(h.strip(), b.strip()) for h, b in zip(parts[1::2], parts[2::2])]
    return head, out


def find(secs, *names):
    for h, b in secs:
        if any(h.lower().startswith(n) for n in names):
            return h, b
    return None, ""


def primary_text_html(body):
    # Drop the trailing "(…word count…)" note lines and keep the paste-ready text.
    lines = [l for l in body.splitlines() if not re.match(r"^\(.*\)$", l.strip())]
    paras = re.split(r"\n\s*\n", "\n".join(lines).strip())
    return "".join(
        "<p>" + "<br>".join(html.escape(l) for l in p.splitlines()) + "</p>" for p in paras if p.strip()
    )


orig = (RUN / "report.html").read_text()


def gallery(ad):
    m = re.search(rf'<article class="ad" id="{ad}">.*?(<div class="gallery">.*?</div>)', orig, re.S)
    return m.group(1) if m else ""


def title_of(text, ad):
    m = re.match(r"#\s*(.+)", text)
    t = m.group(1) if m else ad
    return re.sub(r"^ad_\d+ copy:\s*FINAL\s*", "", t).strip(" ()") or ad


confirm_all = []
articles = []
toc = []
for ad in ADS:
    final = (RW / ad / "final.md").read_text()
    head, secs = sections(final)
    split_at = next((i for i, (h, _) in enumerate(secs) if h.lower().startswith("editor notes")), len(secs))
    copy_secs, note_secs = secs[:split_at], secs[split_at:]

    _, hooks = find(copy_secs, "hooks")
    vis_h, visual = find(copy_secs, "script", "on-image")
    _, prim = find(copy_secs, "primary text")
    _, heads = find(copy_secs, "meta headline")
    _, desc = find(copy_secs, "meta description")
    _, cta = find(copy_secs, "cta")
    _, info = find(copy_secs, "ad info")

    rec = re.search(r"Recommended:?\s*\**(.+?)(?:\n|$)", hooks)
    first_hook = re.search(r"^\|\s*H1\s*\|[^|]*\|\s*([^|]+?)\s*\|", hooks, re.M)
    hook_line = first_hook.group(1).strip() if first_hook else ""

    notes_md = "\n\n".join(f"## {h}\n\n{b}" for h, b in note_secs)
    copy_text = "\n".join(b for _, b in copy_secs)
    confirms = sorted(set(c.strip() for c in re.findall(r"\[CONFIRM:\s*([^\]]+)\]", copy_text) if c.strip(" .")))
    for c in confirms:
        confirm_all.append((ad, c))

    v1 = (RUN / "03-ads" / ad / "copy_final.md").read_text()
    _, v1secs = sections(v1)
    _, v1prim = find(v1secs, "primary text")
    critique = (RW / ad / "critique.md").read_text()

    label, cls = RERENDER[ad]
    fmt = "video" if ad in VIDEO else "image"
    num = ad[-2:]
    name = title_of(final, ad)
    toc.append(f'<a href="#{ad}"><span class="num">{num}</span>{html.escape(hook_line or name)}</a>')

    articles.append(f"""
<article class="ad" id="{ad}">
 <header class="adhead">
  <div class="adid">AD {num}<span class="fmt">{fmt}</span><span class="chip {cls}">{label}</span>{'<span class="chip mid">' + str(len(confirms)) + ' to confirm</span>' if confirms else ''}</div>
  <h3>{html.escape(hook_line or name)}</h3>
  <p class="sub">{html.escape(name)}</p>
 </header>
 {gallery(ad)}
 <div class="cols">
  <div class="block">
   <div class="ptwrap"><h4>Primary text <small>paste-ready</small></h4><button class="copy" type="button" data-target="pt-{ad}">Copy</button></div>
   <div class="pt" id="pt-{ad}">{primary_text_html(prim)}</div>
   <h4>Meta headlines</h4><div class="md">{md(heads)}</div>
   <h4>Meta description · CTA</h4><div class="md">{md(desc)}{md(cta)}</div>
  </div>
  <div class="side">
   <div class="block"><h4>Hooks</h4><div class="md tbl">{md(hooks)}</div></div>
  </div>
 </div>
 <div class="block wide"><h4>{html.escape(vis_h or 'Visual')}</h4><div class="md tbl">{md(visual)}</div></div>
 <details><summary>Ad info: angle, avatar, beliefs</summary><div class="md">{md(info)}</div></details>
 <details><summary>Editor notes: changes, checks, re-render, owner to confirm</summary><div class="md">{md(notes_md)}</div></details>
 <details><summary>Critique of the previous version</summary><div class="md">{md(critique)}</div></details>
 <details><summary>Previous primary text (v1)</summary><div class="pt old">{primary_text_html(v1prim)}</div></details>
</article>""")

n_req = sum(1 for v in RERENDER.values() if v[1] == "bad")
confirm_rows = "".join(
    f'<li><a href="#{ad}">{ad.replace("_", " ").upper()}</a> {html.escape(c)}</li>' for ad, c in confirm_all
)

page = f"""<title>Al Rayan Ring Ads v2</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Public+Sans:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: same campaign ledger as report.html. Summary strip, owner checklist, then one record per ad (creative, paste-ready copy, visual/script, collapsible notes). */
:root {{
 --bg:#f2f4f1; --surface:#ffffff; --ink:#17221b; --muted:#5b6a60; --line:#d7ddd6;
 --accent:#1f5a2e; --accent-soft:#e2ece3; --gold:#a8812f; --warn:#9a5b12; --warn-bg:#fbf0de; --bad:#a3352a; --bad-bg:#f8e3df;
 --display:"Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
 --body:"Public Sans", "Segoe UI", system-ui, sans-serif;
 --mono:"JetBrains Mono", ui-monospace, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
 --bg:#0f1511; --surface:#161e18; --ink:#e6ece7; --muted:#9aa89e; --line:#2a352d;
 --accent:#7fc392; --accent-soft:#1d2d21; --gold:#d6b066; --warn:#f0b766; --warn-bg:#2d2414; --bad:#f09a8c; --bad-bg:#33201c; color-scheme:dark }} }}
:root[data-theme="dark"] {{
 --bg:#0f1511; --surface:#161e18; --ink:#e6ece7; --muted:#9aa89e; --line:#2a352d;
 --accent:#7fc392; --accent-soft:#1d2d21; --gold:#d6b066; --warn:#f0b766; --warn-bg:#2d2414; --bad:#f09a8c; --bad-bg:#33201c; color-scheme:dark }}
body {{ background:var(--bg); color:var(--ink); font:15px/1.6 var(--body); }}
.wrap {{ max-width:1180px; margin:0 auto; padding-inline:clamp(16px,4vw,40px); padding-block:40px 80px; display:grid; gap:36px; }}
a {{ color:var(--accent); }}
a:focus-visible, video:focus-visible, button:focus-visible, summary:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
h1,h2,h3,h4 {{ font-family:var(--display); text-wrap:balance; margin:0; }}
.num {{ font-family:var(--mono); font-variant-numeric:tabular-nums; }}
.top {{ display:grid; gap:18px; }}
.eyebrow {{ font:500 12px/1 var(--mono); letter-spacing:.12em; text-transform:uppercase; color:var(--muted); }}
h1 {{ font-size:clamp(30px,5vw,52px); font-weight:700; line-height:1.05; letter-spacing:-.01em; max-width:20ch; }}
.lede {{ max-width:68ch; color:var(--muted); margin:0; }}
.counter {{ display:flex; flex-wrap:wrap; gap:12px; }}
.cell {{ background:var(--surface); border:1px solid var(--line); border-radius:6px; padding:14px 18px; display:grid; gap:4px; min-width:0; flex:1 1 150px; }}
.cell b {{ font:500 30px/1 var(--mono); font-variant-numeric:tabular-nums; color:var(--accent); }}
.cell span {{ font-size:12px; color:var(--muted); letter-spacing:.04em; text-transform:uppercase; }}
.confirm {{ background:var(--warn-bg); border-radius:8px; padding:18px 22px; display:grid; gap:8px; }}
.confirm h2 {{ font-size:18px; }}
.confirm ul {{ margin:0; padding-left:18px; display:grid; gap:4px; font-size:14px; }}
.confirm a {{ font:500 12px var(--mono); margin-right:6px; }}
.toc {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:8px; }}
.toc a {{ display:flex; gap:10px; align-items:baseline; text-decoration:none; color:var(--ink); padding:10px 12px; border-top:1px solid var(--line); min-width:0; }}
.toc a:hover {{ color:var(--accent); }}
.toc .num {{ color:var(--gold); font-size:13px; }}
section > h2 {{ font-size:22px; margin-bottom:14px; }}
.ad {{ background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:clamp(16px,3vw,28px); display:grid; gap:20px; min-width:0; }}
.adhead {{ display:grid; gap:6px; }}
.adid {{ font:500 13px var(--mono); letter-spacing:.1em; color:var(--gold); display:flex; flex-wrap:wrap; gap:8px; align-items:center; }}
.fmt, .chip {{ font-size:11px; padding:2px 8px; border-radius:99px; text-transform:uppercase; letter-spacing:.06em; }}
.fmt {{ background:var(--accent-soft); color:var(--accent); }}
.chip.ok {{ background:var(--accent-soft); color:var(--accent); }}
.chip.mid {{ background:var(--warn-bg); color:var(--warn); }}
.chip.bad {{ background:var(--bad-bg); color:var(--bad); }}
.adhead h3 {{ font-size:clamp(20px,2.6vw,28px); font-weight:700; }}
.sub {{ margin:0; color:var(--muted); font-size:14px; }}
.gallery {{ display:flex; gap:12px; overflow-x:auto; padding-bottom:4px; }}
.shot {{ margin:0; flex:0 0 auto; width:min(180px,40vw); display:grid; gap:6px; }}
.shot.main {{ width:min(300px,72vw); }}
.shot img, .shot video {{ width:100%; aspect-ratio:9/16; object-fit:cover; border-radius:6px; background:var(--accent-soft); display:block; max-width:100%; }}
figcaption {{ font:500 11px var(--mono); color:var(--muted); text-transform:uppercase; letter-spacing:.06em; }}
.cols {{ display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,1fr); gap:28px; }}
@media (max-width:860px) {{ .cols {{ grid-template-columns:1fr; }} }}
.block {{ display:grid; gap:10px; min-width:0; align-content:start; }}
.side {{ display:grid; gap:20px; align-content:start; min-width:0; }}
h4 {{ font-size:13px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); font-family:var(--body); }}
h4 small {{ font-weight:400; text-transform:none; letter-spacing:0; color:var(--gold); }}
.ptwrap {{ display:flex; justify-content:space-between; align-items:center; gap:12px; }}
.copy {{ font:500 12px var(--mono); background:var(--accent); color:var(--surface); border:0; border-radius:4px; padding:5px 12px; cursor:pointer; }}
.pt {{ background:var(--accent-soft); border-radius:6px; padding:14px 16px; }}
.pt p {{ margin:0 0 .6em; max-width:65ch; }}
.pt p:last-child {{ margin-bottom:0; }}
.pt.old {{ background:transparent; border:1px dashed var(--line); color:var(--muted); }}
.md {{ font-size:14px; min-width:0; }}
.md p, .md ul, .md ol {{ margin:0 0 .6em; }}
.md h2 {{ font-size:16px; margin:1em 0 .4em; }}
.md h3 {{ font-size:14px; margin:1em 0 .3em; }}
.md h1 {{ font-size:18px; margin:0 0 .5em; }}
.tbl {{ overflow-x:auto; }}
.md table {{ border-collapse:collapse; width:100%; font-size:13px; }}
.md th, .md td {{ text-align:left; vertical-align:top; padding:6px 8px; border-bottom:1px solid var(--line); }}
.md th {{ font-size:11px; text-transform:uppercase; letter-spacing:.05em; color:var(--muted); }}
.md code {{ font:500 12px var(--mono); }}
details {{ border-top:1px solid var(--line); padding-top:10px; }}
summary {{ cursor:pointer; font-weight:600; font-size:14px; color:var(--accent); }}
details > div {{ margin-top:12px; }}
.foot {{ font:500 12px var(--mono); color:var(--muted); }}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior:auto; }} }}
</style>
<div class="wrap">
 <header class="top">
  <div class="eyebrow">Al Rayan Dhikr Ring 2.0 · alrayanrings.net · rewrite round 2026-10-12</div>
  <h1>Eleven ads, rewritten</h1>
  <p class="lede">For each ad, a critic, a rewriter and a final editor worked in turn. Before writing, all three read the full market research and the verified Quran and hadith list. They also read the store pages and looked at the creative. The images and videos below are unchanged from the first round. The copy and video scripts are new, and each ad says whether its creative needs a re-render.</p>
  <div class="counter">
   <div class="cell"><b>8+3</b><span>image + video ads</span></div>
   <div class="cell"><b>{n_req}</b><span>images need a re-render</span></div>
   <div class="cell"><b>3</b><span>videos need a new VO only</span></div>
   <div class="cell"><b>{len(confirm_all)}</b><span>claims to confirm</span></div>
  </div>
 </header>
 <section class="confirm" aria-label="Owner to confirm">
  <h2>Confirm before running</h2>
  <ul>{confirm_rows}</ul>
  <p class="sub">If a claim isn't true, delete the tagged sentence. Each ad's editor notes say exactly what to cut. Also check: in ads 04, 05, 07, 08 and 11 the ring appears on the index or middle finger, sometimes on a male-looking hand. Re-roll those shots before scaling.</p>
 </section>
 <nav class="toc" aria-label="Ads">{''.join(toc)}</nav>
 <section><h2>The ads</h2><div style="display:grid;gap:28px">{''.join(articles)}</div></section>
 <p class="foot">Source files: 05-rewrite/ad_XX/final.md (copy), critique.md, rewrite.md. Original report: report.html.</p>
</div>
<script>
document.querySelectorAll('.copy').forEach(function (b) {{
  b.addEventListener('click', function () {{
    var el = document.getElementById(b.dataset.target);
    var text = Array.from(el.querySelectorAll('p')).map(function (p) {{ return p.innerText; }}).join('\\n\\n');
    var done = function () {{ b.textContent = 'Copied'; setTimeout(function () {{ b.textContent = 'Copy'; }}, 1500); }};
    try {{
      navigator.clipboard.writeText(text).then(done, function () {{ select(el); }});
    }} catch (e) {{ select(el); }}
  }});
}});
function select(el) {{ var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }}
</script>
"""
OUT.write_text(page)
print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB), {len(confirm_all)} confirm tags")
