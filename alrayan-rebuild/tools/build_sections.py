"""Generates the Al Rayan ar-* Shopify sections (markup + {% schema %}) and the two JSON templates."""
import json, os

ROOT = '/home/user/smth/alrayan-rebuild/shopify'
ICONS = json.load(open('/home/user/smth/work/icon_options.json'))
PRODUCT_HANDLE = 'elegant-metal-intelligent-rings-with-digital-display-vibration-alerts-precise-prayer-warning-for-islamic-prayer-trackings'


def img(name):
    return f'shopify://shop_images/{name}'


# ---------------- schema helpers ----------------
def t(id, label, default=None, info=None):
    d = {'type': 'text', 'id': id, 'label': label}
    if default is not None: d['default'] = default
    if info: d['info'] = info
    return d

def ta(id, label, default=None, info=None):
    d = t(id, label, default, info); d['type'] = 'textarea'; return d

def rt(id, label, default=None):
    d = {'type': 'richtext', 'id': id, 'label': label}
    if default is not None: d['default'] = default
    return d

def irt(id, label, default=None, info=None):
    d = {'type': 'inline_richtext', 'id': id, 'label': label}
    if default is not None: d['default'] = default
    if info: d['info'] = info
    return d

def image(id, label='Image', info=None):
    d = {'type': 'image_picker', 'id': id, 'label': label}
    if info: d['info'] = info
    return d

def url(id, label):
    return {'type': 'url', 'id': id, 'label': label}

def product(id='product', label='Product', info='Buttons link here and show its price.'):
    return {'type': 'product', 'id': id, 'label': label, 'info': info}

def cb(id, label, default=True, info=None):
    d = {'type': 'checkbox', 'id': id, 'label': label, 'default': default}
    if info: d['info'] = info
    return d

def icon(id='icon', label='Icon', default='sparkle'):
    return {'type': 'select', 'id': id, 'label': label, 'options': ICONS, 'default': default}

def header(content):
    return {'type': 'header', 'content': content}

def bg(default='ar--white'):
    return {'type': 'select', 'id': 'background', 'label': 'Background', 'default': default, 'options': [
        {'value': 'ar--white', 'label': 'White'}, {'value': 'ar--paper', 'label': 'Paper'},
        {'value': 'ar--cream', 'label': 'Cream'}, {'value': 'ar--green', 'label': 'Brand green'}]}

ANCHOR = t('anchor_id', 'Anchor ID', info='Optional. Lets other buttons link here with #your-id.')

CTA_LIQUID = """{%- liquid
  assign cta_product = section.settings.product
  if cta_product == blank and product != blank
    assign cta_product = product
  endif
  assign cta_url = section.settings.button_link
  if template.name == 'product'
    assign cta_url = '#ar-buy'
  elsif cta_product != blank
    assign cta_url = cta_product.url
  endif
  if cta_url == blank
    assign cta_url = routes.all_products_collection_url
  endif
  assign cta_label = section.settings.button_label
  if section.settings.show_price and cta_product != blank
    assign cta_label = cta_label | append: ' · ' | append: cta_product.price | money
  endif
-%}"""
# NB: `append: x | money` would money-format the whole string, so price is formatted separately below.
CTA_LIQUID = CTA_LIQUID.replace(
    "    assign cta_label = cta_label | append: ' · ' | append: cta_product.price | money\n",
    "    assign cta_price = cta_product.price | money\n    assign cta_label = cta_label | append: ' · ' | append: cta_price\n")

CTA_SETTINGS = lambda label, show_price=True: [
    header('Button'), t('button_label', 'Button label', label), product(),
    url('button_link', 'Fallback link'), cb('show_price', 'Show price on button', show_price)]

ASSURANCE = """<ul class="ar-assurance">
          {%- for i in (1..3) -%}
            {%- assign key = 'assurance_' | append: i -%}
            {%- if section.settings[key] != blank -%}
              <li><span>{% render 'ar-icon', name: 'check' %}{{ section.settings[key] }}</span></li>
            {%- endif -%}
          {%- endfor -%}
        </ul>"""
ASSURANCE_SETTINGS = [header('Reassurance line'), t('assurance_1', 'Item 1', 'Free US shipping'),
                      t('assurance_2', 'Item 2', '60-day money-back guarantee'), t('assurance_3', 'Item 3', '1-year warranty')]

OPEN = """{%- render 'ar-assets' -%}
<section class="ar ar-section {{ section.settings.background }}"{% if section.settings.anchor_id != blank %} id="{{ section.settings.anchor_id | handleize }}"{% endif %}>"""

HEAD = """<div class="ar-head" data-ar-reveal>
      {%- if section.settings.eyebrow != blank -%}<p class="ar-eyebrow">{{ section.settings.eyebrow }}</p>{%- endif -%}
      {%- if section.settings.heading != blank -%}<h2 class="ar-h2">{{ section.settings.heading }}</h2>{%- endif -%}
      {%- if section.settings.text != blank -%}<div class="ar-lead">{{ section.settings.text }}</div>{%- endif -%}
    </div>"""

def head_settings(eyebrow, heading, text=None):
    s = [t('eyebrow', 'Eyebrow', eyebrow), irt('heading', 'Heading', heading, info='Wrap words in italics to highlight them in green.')]
    if text is not None: s.append(rt('text', 'Text', text))
    return s


SECTIONS = {}

# ---------------- hero ----------------
SECTIONS['ar-hero'] = dict(markup=CTA_LIQUID + """
{%- render 'ar-assets' -%}
<section class="ar ar-hero"{% if section.settings.anchor_id != blank %} id="{{ section.settings.anchor_id | handleize }}"{% endif %}>
  <div class="ar-container ar-hero__grid">
    <div class="ar-hero__copy">
      {%- if section.settings.rating_text != blank -%}
        <p class="ar-rating">{% render 'ar-stars' %}<span>{{ section.settings.rating_text }}</span></p>
      {%- endif -%}
      <h1 class="ar-h1">{{ section.settings.heading }}</h1>
      <div class="ar-lead">{{ section.settings.text }}</div>
      <div class="ar-hero__ctas">
        <a class="ar-btn" href="{{ cta_url }}">{{ cta_label }}{% render 'ar-icon', name: 'arrow' %}</a>
        {%- if section.settings.secondary_label != blank -%}
          <a class="ar-link" href="{{ section.settings.secondary_link | default: '#' }}">{{ section.settings.secondary_label }}</a>
        {%- endif -%}
      </div>
      """ + ASSURANCE + """
    </div>
    <div class="ar-hero__visual">
      <div class="ar-media ar-media--arch">
        {%- render 'ar-image', image: section.settings.image, alt: section.settings.image_alt, sizes: '(min-width: 990px) 45vw, 90vw', loading: 'eager', placeholder: 'product-1' -%}
      </div>
      {%- if section.settings.chip_1_title != blank -%}
        <div class="ar-chip ar-chip--a"><span class="ar-chip__dot">{% render 'ar-icon', name: 'vibrate' %}</span><span><strong>{{ section.settings.chip_1_title }}</strong>{{ section.settings.chip_1_text }}</span></div>
      {%- endif -%}
      {%- if section.settings.chip_2_title != blank -%}
        <div class="ar-chip ar-chip--b"><span class="ar-chip__dot">{% render 'ar-icon', name: 'drop' %}</span><span><strong>{{ section.settings.chip_2_title }}</strong>{{ section.settings.chip_2_text }}</span></div>
      {%- endif -%}
    </div>
  </div>
</section>""", schema={
    'name': 'AR · Hero', 'tag': 'div',
    'settings': [
        t('rating_text', 'Rating text', '4.9 · Worn by 8,200+ Muslims'),
        irt('heading', 'Heading', 'Keep your tongue moist with <em>dhikr</em>'),
        rt('text', 'Text', '<p>A featherlight smart ring that counts every tasbih with a silent tap of your thumb and vibrates gently at 33, 66 and 99. Keep remembering Allah on the train, at your desk and between meetings, without your phone or a clicker.</p>'),
        *CTA_SETTINGS('Shop the Dhikr Ring'),
        t('secondary_label', 'Secondary link label', 'See how it works'),
        t('secondary_link', 'Secondary link', '#how-it-works', info='A page URL or #anchor-id of a section on this page.'),
        *ASSURANCE_SETTINGS,
        header('Image'), image('image'), t('image_alt', 'Image alt text', 'Al Rayan Dhikr Rings in black and rose gold'),
        header('Floating notes'),
        t('chip_1_title', 'Note 1 title', 'Vibrates at 33 · 66 · 99'), t('chip_1_text', 'Note 1 text', 'No need to look down'),
        t('chip_2_title', 'Note 2 title', 'IP67 water resistant'), t('chip_2_text', 'Note 2 text', 'Keep it on for wudu'),
        ANCHOR,
    ],
    'presets': [{'name': 'AR · Hero'}]})

# ---------------- trust bar ----------------
SECTIONS['ar-trust-bar'] = dict(markup="""{%- render 'ar-assets' -%}
<section class="ar ar-trustbar">
  <ul class="ar-container ar-trustbar__list">
    {%- for block in section.blocks -%}
      <li class="ar-trustbar__item" {{ block.shopify_attributes }}>{% render 'ar-icon', name: block.settings.icon %}<span>{{ block.settings.text }}</span></li>
    {%- endfor -%}
  </ul>
</section>""", schema={
    'name': 'AR · Trust bar', 'tag': 'div', 'max_blocks': 6,
    'settings': [],
    'blocks': [{'type': 'item', 'name': 'Item', 'settings': [icon(default='shield'), t('text', 'Text', 'Free US shipping')]}],
    'presets': [{'name': 'AR · Trust bar', 'blocks': [
        {'type': 'item', 'settings': {'icon': 'shield', 'text': '60-day money-back guarantee'}},
        {'type': 'item', 'settings': {'icon': 'truck', 'text': 'Free US shipping'}},
        {'type': 'item', 'settings': {'icon': 'drop', 'text': 'IP67 water resistant'}},
        {'type': 'item', 'settings': {'icon': 'battery', 'text': '3–5 days per charge'}},
        {'type': 'item', 'settings': {'icon': 'chat', 'text': 'US-based support'}},
    ]}]})

# ---------------- intention / problem ----------------
SECTIONS['ar-intention'] = dict(markup=OPEN + """
  <div class="ar-container">
    """ + HEAD + """
    {%- if section.settings.quote != blank -%}
      <figure class="ar-quote" data-ar-reveal>
        <p>{{ section.settings.quote }}</p>
        {%- if section.settings.quote_source != blank -%}<cite>{{ section.settings.quote_source }}</cite>{%- endif -%}
      </figure>
    {%- endif -%}
    <div class="ar-cards3">
      {%- for block in section.blocks -%}
        <div class="ar-card" data-ar-reveal {{ block.shopify_attributes }}>
          <span class="ar-card__icon">{% render 'ar-icon', name: block.settings.icon %}</span>
          <h3>{{ block.settings.title }}</h3>
          <p>{{ block.settings.text }}</p>
        </div>
      {%- endfor -%}
    </div>
    {%- if section.settings.bridge != blank -%}
      <div class="ar-bridge" data-ar-reveal>
        <p>{{ section.settings.bridge }}</p>
        {%- if section.settings.link_label != blank -%}<a class="ar-link" href="{{ section.settings.link | default: '#' }}">{{ section.settings.link_label }}</a>{%- endif -%}
      </div>
    {%- endif -%}
  </div>
</section>""", schema={
    'name': 'AR · Intention', 'tag': 'div', 'max_blocks': 3,
    'settings': [
        *head_settings('It’s not your intention', 'Struggling to stay consistent? <em>Blame the tools, not your heart.</em>',
                       '<p>Most of us don’t lack the will to remember Allah. We lose count when someone interrupts, the beads stay at home, the clicker is too loud for the office, and opening an app means opening every notification with it.</p>'),
        header('Quote'),
        t('quote', 'Quote', '“Let your tongue remain moist with the remembrance of Allah.”'),
        t('quote_source', 'Source', 'The Prophet ﷺ · Jami‘ at-Tirmidhi'),
        header('Closing line'),
        t('bridge', 'Closing line', 'Al Rayan was made for the moments in between, one quiet tap at a time.'),
        t('link_label', 'Link label', 'See how it works'), t('link', 'Link', '#how-it-works'),
        bg('ar--paper'), ANCHOR,
    ],
    'blocks': [{'type': 'card', 'name': 'Card', 'settings': [icon(), t('title', 'Title'), ta('text', 'Text')]}],
    'presets': [{'name': 'AR · Intention', 'blocks': [
        {'type': 'card', 'settings': {'icon': 'beads', 'title': 'The beads stay at home', 'text': 'A misbaha is beautiful, but it rarely makes it to the office, the gym or the school run.'}},
        {'type': 'card', 'settings': {'icon': 'volume', 'title': 'The clicker is too loud', 'text': 'In a quiet meeting or library, every click feels like an announcement.'}},
        {'type': 'card', 'settings': {'icon': 'phone', 'title': 'The app pulls you in', 'text': 'Open a tasbih app and the messages and notifications are waiting right behind it.'}},
    ]}]})

# ---------------- moments ----------------
SECTIONS['ar-moments'] = dict(markup=OPEN + """
  <div class="ar-container">
    """ + HEAD + """
    <div class="ar-moments">
      {%- for block in section.blocks -%}
        <article class="ar-moment" data-ar-reveal {{ block.shopify_attributes }}>
          <div class="ar-media ar-media--arch">
            {%- render 'ar-image', image: block.settings.image, sizes: '(min-width: 850px) 33vw, 78vw', placeholder: 'lifestyle-2' -%}
          </div>
          {%- if block.settings.tag != blank -%}<p class="ar-moment__tag">{{ block.settings.tag }}</p>{%- endif -%}
          <h3>{{ block.settings.title }}</h3>
          <p>{{ block.settings.text }}</p>
        </article>
      {%- endfor -%}
    </div>
  </div>
</section>""", schema={
    'name': 'AR · Moments', 'tag': 'div', 'max_blocks': 3,
    'settings': [*head_settings('Made for real days', 'Dhikr that fits <em>in between</em>',
                                '<p>No new routine to build. Just the minutes you already have.</p>'),
                 bg('ar--white'), ANCHOR],
    'blocks': [{'type': 'moment', 'name': 'Moment', 'settings': [image('image'), t('tag', 'Label'), t('title', 'Title'), ta('text', 'Text')]}],
    'presets': [{'name': 'AR · Moments', 'blocks': [
        {'type': 'moment', 'settings': {'tag': 'The commute', 'title': 'Finish your istighfar before your stop', 'text': 'Thumb on the button, phone in your pocket. The ring keeps the count while you keep your eyes up.'}},
        {'type': 'moment', 'settings': {'tag': 'At work', 'title': 'Dhikr between meetings, without a sound', 'text': 'No click, no screen on the desk. To everyone else it’s simply a ring.'}},
        {'type': 'moment', 'settings': {'tag': 'At home', 'title': 'Pick up right where you left off', 'text': 'The kids call, the kettle boils. Your count waits on your finger until you come back.'}},
    ]}]})

# ---------------- features ----------------
SECTIONS['ar-features'] = dict(markup=OPEN + """
  <div class="ar-container">
    <div class="ar-features">
      <div class="ar-media" data-ar-reveal>
        {%- render 'ar-image', image: section.settings.image, sizes: '(min-width: 990px) 45vw, 100vw', placeholder: 'product-2' -%}
      </div>
      <div>
        """ + HEAD.replace('class="ar-head"', 'class="ar-head ar-head--left"') + """
        <div class="ar-features__list">
          {%- for block in section.blocks -%}
            <div class="ar-feature" data-ar-reveal {{ block.shopify_attributes }}>
              <span class="ar-feature__icon">{% render 'ar-icon', name: block.settings.icon %}</span>
              <h3>{{ block.settings.title }}</h3>
              <p>{{ block.settings.text }}</p>
            </div>
          {%- endfor -%}
        </div>
      </div>
    </div>
    {%- if section.settings.spec_1_value != blank -%}
      <dl class="ar-specs" data-ar-reveal>
        {%- for i in (1..4) -%}
          {%- assign v = 'spec_' | append: i | append: '_value' -%}
          {%- assign l = 'spec_' | append: i | append: '_label' -%}
          {%- if section.settings[v] != blank -%}
            <div class="ar-spec"><dt><strong>{{ section.settings[v] }}</strong></dt><dd><span>{{ section.settings[l] }}</span></dd></div>
          {%- endif -%}
        {%- endfor -%}
      </dl>
    {%- endif -%}
  </div>
</section>""", schema={
    'name': 'AR · Features', 'tag': 'div', 'max_blocks': 6,
    'settings': [
        image('image'),
        *head_settings('The Dhikr Ring 2.0', 'Everything a tasbih does. <em>Nothing it doesn’t need.</em>', ''),
        header('Spec strip'),
        t('spec_1_value', 'Spec 1 value', '99,999'), t('spec_1_label', 'Spec 1 label', 'count memory'),
        t('spec_2_value', 'Spec 2 value', 'IP67'), t('spec_2_label', 'Spec 2 label', 'water resistant'),
        t('spec_3_value', 'Spec 3 value', '3–5 days'), t('spec_3_label', 'Spec 3 label', 'battery, frequent use'),
        t('spec_4_value', 'Spec 4 value', '3 sizes'), t('spec_4_label', 'Spec 4 label', '18 · 20 · 22mm'),
        bg('ar--cream'), ANCHOR,
    ],
    'blocks': [{'type': 'feature', 'name': 'Feature', 'settings': [icon(), t('title', 'Title'), ta('text', 'Text')]}],
    'presets': [{'name': 'AR · Features', 'blocks': [
        {'type': 'feature', 'settings': {'icon': 'tap', 'title': 'Silent thumb tap', 'text': 'A soft side button counts every recitation without a sound.'}},
        {'type': 'feature', 'settings': {'icon': 'vibrate', 'title': 'Feel 33, 66 and 99', 'text': 'A gentle vibration marks each milestone, so you never need to look down.'}},
        {'type': 'feature', 'settings': {'icon': 'clock', 'title': 'Prayer-time alerts', 'text': 'A quiet buzz for each of the five daily prayers, even with your phone on silent.'}},
        {'type': 'feature', 'settings': {'icon': 'drop', 'title': 'Keep it on for wudu', 'text': 'IP67 water resistance means it stays on your finger at the sink.'}},
        {'type': 'feature', 'settings': {'icon': 'refresh', 'title': 'Never lose your place', 'text': 'Your count stays on the ring when life interrupts, up to 99,999.'}},
        {'type': 'feature', 'settings': {'icon': 'cloud', 'title': 'Your history in the app', 'text': 'Sync over Bluetooth whenever you like to see daily and monthly totals.'}},
    ]}]})

# ---------------- how it works ----------------
SECTIONS['ar-how'] = dict(markup=OPEN + """
  <div class="ar-container">
    """ + HEAD + """
    <ol class="ar-steps">
      {%- for block in section.blocks -%}
        <li class="ar-step" data-ar-reveal {{ block.shopify_attributes }}>
          <div class="ar-media">
            {%- render 'ar-image', image: block.settings.image, sizes: '(min-width: 850px) 33vw, 100vw', placeholder: 'lifestyle-1' -%}
          </div>
          <h3 class="ar-step__num"><span>{{ forloop.index }}</span>{{ block.settings.title }}</h3>
          <p>{{ block.settings.text }}</p>
        </li>
      {%- endfor -%}
    </ol>
  </div>
</section>""", schema={
    'name': 'AR · How it works', 'tag': 'div', 'max_blocks': 4,
    'settings': [*head_settings('How it works', 'Three steps to <em>consistent dhikr</em>',
                                '<p>How the Dhikr Ring 2.0 fits into the day you already have.</p>'),
                 bg('ar--white'), {**ANCHOR, 'default': 'how-it-works'}],
    'blocks': [{'type': 'step', 'name': 'Step', 'settings': [image('image'), t('title', 'Title'), ta('text', 'Text')]}],
    'presets': [{'name': 'AR · How it works', 'blocks': [
        {'type': 'step', 'settings': {'title': 'Wear', 'text': 'Slip it onto the finger that feels natural. Most people choose the index finger so the thumb rests on the button; the ring finger works well too.'}},
        {'type': 'step', 'settings': {'title': 'Tap', 'text': 'Press the side button with your thumb for each tasbih. A gentle vibration at 33, 66 and 99 lets you keep your attention on the words.'}},
        {'type': 'step', 'settings': {'title': 'Review', 'text': 'Open the Al Rayan app whenever you like to sync over Bluetooth and see your daily and monthly totals.'}},
    ]}]})

# ---------------- comparison ----------------
CELL = """{%- case VAL -%}
              {%- when 'yes' -%}<span class="ar-yes"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span><span class="ar-sr">Yes</span>
              {%- when 'some' -%}<span class="ar-some" aria-hidden="true">~</span><span class="ar-sr">Partly</span>
              {%- else -%}<span class="ar-no"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg></span><span class="ar-sr">No</span>
            {%- endcase -%}"""
YN = lambda id, label, default: {'type': 'select', 'id': id, 'label': label, 'default': default, 'options': [
    {'value': 'yes', 'label': 'Yes'}, {'value': 'some', 'label': 'Partly'}, {'value': 'no', 'label': 'No'}]}
SECTIONS['ar-comparison'] = dict(markup=OPEN + """
  <div class="ar-container">
    """ + HEAD + """
    <div class="ar-compare-wrap" data-ar-reveal>
      <table class="ar-compare">
        <thead>
          <tr>
            <th scope="col"><span class="ar-sr">Feature</span></th>
            <th scope="col" class="ar-col-us">{{ section.settings.us_label }}</th>
            <th scope="col">{{ section.settings.col_1 }}</th>
            <th scope="col">{{ section.settings.col_2 }}</th>
            <th scope="col">{{ section.settings.col_3 }}</th>
          </tr>
        </thead>
        <tbody>
          {%- for block in section.blocks -%}
            <tr {{ block.shopify_attributes }}>
              <td>{{ block.settings.label }}</td>
              <td class="ar-col-us">""" + CELL.replace('VAL', 'block.settings.us') + """</td>
              <td>""" + CELL.replace('VAL', 'block.settings.c1') + """</td>
              <td>""" + CELL.replace('VAL', 'block.settings.c2') + """</td>
              <td>""" + CELL.replace('VAL', 'block.settings.c3') + """</td>
            </tr>
          {%- endfor -%}
        </tbody>
      </table>
    </div>
    {%- if section.settings.legend != blank -%}<p class="ar-compare-legend">{{ section.settings.legend }}</p>{%- endif -%}
    {%- if section.settings.note != blank -%}
      <div class="ar-compare-note" data-ar-reveal>{% render 'ar-icon', name: 'heart' %}<div>{{ section.settings.note }}</div></div>
    {%- endif -%}
  </div>
</section>""", schema={
    'name': 'AR · Comparison', 'tag': 'div', 'max_blocks': 10,
    'settings': [
        *head_settings('How it compares', 'Every tool has its place. <em>This one goes everywhere.</em>', ''),
        t('us_label', 'Your column', 'Al Rayan Ring'), t('col_1', 'Column 2', 'Misbaha'),
        t('col_2', 'Column 3', 'Plastic clicker'), t('col_3', 'Column 4', 'Phone app'),
        t('legend', 'Legend', '~ Partly, depends on the model or app'),
        rt('note', 'Note under table', '<p><strong>Counting on your fingers is the Sunnah, and nothing replaces it.</strong> Many of our customers use their fingers for the adhkar after salah and the ring for larger daily goals, like 1,000 istighfar on the way to work.</p>'),
        bg('ar--paper'), ANCHOR,
    ],
    'blocks': [{'type': 'row', 'name': 'Row', 'settings': [t('label', 'Feature'), YN('us', 'Al Rayan', 'yes'), YN('c1', 'Column 2', 'no'), YN('c2', 'Column 3', 'no'), YN('c3', 'Column 4', 'no')]}],
    'presets': [{'name': 'AR · Comparison', 'blocks': [
        {'type': 'row', 'settings': {'label': 'Silent in meetings and classes', 'us': 'yes', 'c1': 'yes', 'c2': 'no', 'c3': 'some'}},
        {'type': 'row', 'settings': {'label': 'Worn all day, nothing to carry', 'us': 'yes', 'c1': 'no', 'c2': 'no', 'c3': 'no'}},
        {'type': 'row', 'settings': {'label': 'Keeps your count when interrupted', 'us': 'yes', 'c1': 'no', 'c2': 'yes', 'c3': 'yes'}},
        {'type': 'row', 'settings': {'label': 'Works without your phone', 'us': 'yes', 'c1': 'yes', 'c2': 'yes', 'c3': 'no'}},
        {'type': 'row', 'settings': {'label': 'Vibrates at 33, 66 and 99', 'us': 'yes', 'c1': 'no', 'c2': 'no', 'c3': 'some'}},
        {'type': 'row', 'settings': {'label': 'Prayer-time alerts', 'us': 'yes', 'c1': 'no', 'c2': 'no', 'c3': 'yes'}},
        {'type': 'row', 'settings': {'label': 'Stays on for wudu', 'us': 'yes', 'c1': 'no', 'c2': 'no', 'c3': 'no'}},
    ]}]})

# ---------------- reviews ----------------
SECTIONS['ar-reviews'] = dict(markup=OPEN + """
  <div class="ar-container">
    <div class="ar-reviews__top">
      """ + HEAD.replace('class="ar-head"', 'class="ar-head ar-head--left" style="margin-bottom:0"') + """
      {%- if section.settings.score != blank -%}
        <div class="ar-score" data-ar-reveal>
          <span class="ar-score__num">{{ section.settings.score }}</span>
          <span class="ar-score__meta">{% render 'ar-stars' %}<span>{{ section.settings.score_text }}</span></span>
        </div>
      {%- endif -%}
    </div>
    <div class="ar-reviews__grid">
      {%- for block in section.blocks -%}
        <figure class="ar-review" data-ar-reveal {{ block.shopify_attributes }}>
          {%- if block.settings.image != blank -%}
            <div class="ar-media">{%- render 'ar-image', image: block.settings.image, sizes: '(min-width: 850px) 33vw, 82vw' -%}</div>
          {%- else -%}<div></div>{%- endif -%}
          <div class="ar-review__body">
            {%- render 'ar-stars' -%}
            <blockquote class="ar-review__text">{{ block.settings.text }}</blockquote>
            <figcaption class="ar-review__who">
              <span><strong>{{ block.settings.author }}</strong>{% if block.settings.location != blank %} · {{ block.settings.location }}{% endif %}</span>
              {%- if block.settings.verified -%}<span class="ar-verified">{% render 'ar-icon', name: 'check' %}Verified buyer</span>{%- endif -%}
            </figcaption>
          </div>
        </figure>
      {%- endfor -%}
    </div>
  </div>
</section>""", schema={
    'name': 'AR · Reviews', 'tag': 'div', 'max_blocks': 9,
    'settings': [
        *head_settings('Voices from the community', 'Loved by <em>8,200+</em> Muslim wearers', '<p>How Muslims across America are keeping their remembrance close.</p>'),
        t('score', 'Average rating', '4.9'), t('score_text', 'Rating caption', 'average from 8,200+ wearers'),
        bg('ar--white'), {**ANCHOR, 'default': 'reviews'},
    ],
    'blocks': [{'type': 'review', 'name': 'Review', 'settings': [
        image('image', 'Photo'), ta('text', 'Review'), t('author', 'Name'), t('location', 'Location'),
        cb('verified', 'Show “Verified buyer”', False, info='Only tick for reviews from real orders.')]}],
    'presets': [{'name': 'AR · Reviews', 'blocks': [
        {'type': 'review', 'settings': {'text': 'I work in a fast-paced office in Chicago. This ring is a lifesaver for keeping my dhikr consistent between meetings without looking unprofessional.', 'author': 'Michael J.', 'location': 'Chicago'}},
        {'type': 'review', 'settings': {'text': 'The vibration at 33 counts is perfect. I don’t have to look down at all. It has changed my commute through NYC entirely.', 'author': 'Ashley M.', 'location': 'New York'}},
        {'type': 'review', 'settings': {'text': 'Solid build quality. I was worried it would feel like a toy, but it feels like a real piece of tech. Very happy with my purchase.', 'author': 'David B.'}},
        {'type': 'review', 'settings': {'text': 'The battery actually lasts. I only charge it twice a week. It has finally helped me hit my goal of 1,000 istighfar a day.', 'author': 'Sarah W.'}},
        {'type': 'review', 'settings': {'text': 'Finally, a tasbih that fits my style. It’s modern, sleek and serves the best purpose possible. Highly recommend to any young professional.', 'author': 'Omar', 'location': 'Brooklyn'}},
        {'type': 'review', 'settings': {'text': 'The prayer alerts are so helpful when I’m deep in work. It’s a gentle nudge to take a break and reconnect with Allah.', 'author': 'Amara', 'location': 'Manhattan'}},
    ]}]})

# ---------------- founder ----------------
MARK = """<svg viewBox="0 0 280 280" aria-hidden="true"><circle cx="140" cy="140" r="85" fill="none" stroke="#1F5A2E" stroke-width="30"/><path d="M109 190V138A62 62 0 0 1 140 84.31 62 62 0 0 1 171 138V190Z" fill="#C9A455"/><circle cx="200.1" cy="79.9" r="19.2" fill="#FFFFFF"/><circle cx="200.1" cy="79.9" r="15" fill="#C9A455"/></svg>"""
SECTIONS['ar-founder'] = dict(markup=OPEN + """
  <div class="ar-container">
    <div class="ar-founder">
      <div class="ar-media ar-media--arch" data-ar-reveal>
        {%- render 'ar-image', image: section.settings.image, sizes: '(min-width: 850px) 38vw, 90vw', placeholder: 'lifestyle-1' -%}
      </div>
      <div class="ar-founder__copy" data-ar-reveal>
        {%- if section.settings.eyebrow != blank -%}<p class="ar-eyebrow">{{ section.settings.eyebrow }}</p>{%- endif -%}
        <blockquote>{{ section.settings.quote }}</blockquote>
        <p class="ar-founder__sig"><strong>{{ section.settings.name }}</strong>{{ section.settings.role }}</p>
        {%- if section.settings.name_note != blank -%}
          <div class="ar-name-note">""" + MARK + """<div>{{ section.settings.name_note }}</div></div>
        {%- endif -%}
      </div>
    </div>
  </div>
</section>""", schema={
    'name': 'AR · Founder story', 'tag': 'div',
    'settings': [
        image('image', 'Image', info='A photo of you, your hands wearing the ring, or packing orders works best.'),
        t('eyebrow', 'Eyebrow', 'Our story'),
        ta('quote', 'Story', '“I started Al Rayan as a young Muslim woman learning to navigate life with resilience and faith. It’s more than a small business to me: every ring helps me build my future, and helps someone remember Allah a little more throughout their day.”'),
        t('name', 'Name', 'From our founder'), t('role', 'Role', 'Al Rayan Rings'),
        rt('name_note', 'Name note', '<p><strong>Why “Al Rayan”?</strong> Ar-Rayyan is the gate of Jannah the Prophet ﷺ described for those who fast. Our name is a reminder that small, steady acts are the ones that matter.</p>'),
        bg('ar--cream'), ANCHOR,
    ],
    'presets': [{'name': 'AR · Founder story'}]})

# ---------------- guarantee ----------------
SECTIONS['ar-guarantee'] = dict(markup=CTA_LIQUID + OPEN + """
  <div class="ar-container">
    <div class="ar-guarantee">
      <svg class="ar-seal" viewBox="0 0 200 200" role="img" aria-label="{{ section.settings.days }}-day money-back guarantee">
        <defs><path id="ar-seal-{{ section.id }}" d="M100 100m-77 0a77 77 0 1 1 154 0a77 77 0 1 1-154 0"/></defs>
        <circle cx="100" cy="100" r="98" fill="#C9A455"/>
        <circle cx="100" cy="100" r="62" fill="#163F21"/>
        <circle cx="100" cy="100" r="67" fill="none" stroke="#14201A" stroke-opacity=".35" stroke-dasharray="1.5 4"/>
        <text font-family="Inter, system-ui, sans-serif" font-size="12" font-weight="600" letter-spacing="2.6" fill="#14201A"><textPath href="#ar-seal-{{ section.id }}">MONEY-BACK GUARANTEE · MONEY-BACK GUARANTEE ·</textPath></text>
        <text x="100" y="108" text-anchor="middle" font-family="'Cormorant Garamond', Georgia, serif" font-size="58" font-weight="600" fill="#F6F1E6">{{ section.settings.days }}</text>
        <text x="100" y="131" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" font-weight="600" letter-spacing="3.5" fill="#C9A455">DAYS</text>
      </svg>
      <div class="ar-guarantee__copy" data-ar-reveal>
        {%- if section.settings.eyebrow != blank -%}<p class="ar-eyebrow">{{ section.settings.eyebrow }}</p>{%- endif -%}
        <h2 class="ar-h2">{{ section.settings.heading }}</h2>
        <div class="ar-lead">{{ section.settings.text }}</div>
        <ul class="ar-guarantee__perks">
          {%- for i in (1..4) -%}
            {%- assign key = 'perk_' | append: i -%}
            {%- if section.settings[key] != blank -%}<li>{% render 'ar-icon', name: 'check' %}{{ section.settings[key] }}</li>{%- endif -%}
          {%- endfor -%}
        </ul>
        {%- if section.settings.button_label != blank -%}<a class="ar-btn ar-btn--gold" href="{{ cta_url }}">{{ cta_label }}</a>{%- endif -%}
      </div>
    </div>
  </div>
</section>""", schema={
    'name': 'AR · Guarantee', 'tag': 'div',
    'settings': [
        t('days', 'Days', '60'),
        t('eyebrow', 'Eyebrow', 'Our promise'),
        irt('heading', 'Heading', '<em>60 days</em> to make it part of your day'),
        rt('text', 'Text', '<p>Wear it to work, on the commute and at home. If it doesn’t help you stay consistent with your dhikr, send it back within 60 days for a full refund or a different size. No questions asked.</p>'),
        t('perk_1', 'Perk 1', '60-day money-back guarantee'), t('perk_2', 'Perk 2', 'Free returns from anywhere in the US'),
        t('perk_3', 'Perk 3', 'Free size exchanges'), t('perk_4', 'Perk 4', 'One-year tech warranty'),
        *CTA_SETTINGS('Try it for 60 days', False),
        bg('ar--green'), ANCHOR,
    ],
    'presets': [{'name': 'AR · Guarantee'}]})

# ---------------- faq ----------------
SECTIONS['ar-faq'] = dict(markup=OPEN + """
  <div class="ar-container">
    <div class="ar-faq">
      <div class="ar-faq__intro">
        {%- if section.settings.eyebrow != blank -%}<p class="ar-eyebrow">{{ section.settings.eyebrow }}</p>{%- endif -%}
        <h2 class="ar-h2">{{ section.settings.heading }}</h2>
        <div class="ar-lead">{{ section.settings.text }}</div>
        {%- if section.settings.link_label != blank -%}<p><a class="ar-link" href="{{ section.settings.link | default: '/pages/contact' }}">{{ section.settings.link_label }}</a></p>{%- endif -%}
      </div>
      <div class="ar-faq__list">
        {%- for block in section.blocks -%}
          <details {{ block.shopify_attributes }}{% if forloop.first and section.settings.open_first %} open{% endif %}>
            <summary>{{ block.settings.question }}</summary>
            <div class="ar-faq__answer">{{ block.settings.answer }}</div>
          </details>
        {%- endfor -%}
      </div>
    </div>
  </div>
  <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {%- for block in section.blocks -%}
        {"@type":"Question","name":{{ block.settings.question | json }},"acceptedAnswer":{"@type":"Answer","text":{{ block.settings.answer | strip_html | json }}}}{% unless forloop.last %},{% endunless %}
      {%- endfor -%}
    ]}
  </script>
</section>""", schema={
    'name': 'AR · FAQ', 'tag': 'div', 'max_blocks': 14,
    'settings': [
        t('eyebrow', 'Eyebrow', 'FAQ'),
        irt('heading', 'Heading', 'Questions, <em>answered</em>'),
        rt('text', 'Text', '<p>Can’t find what you need? We’re a small, US-based team and we reply to every message.</p>'),
        t('link_label', 'Link label', 'Contact us'), url('link', 'Link'),
        cb('open_first', 'Open the first question', True),
        bg('ar--white'), {**ANCHOR, 'default': 'faq'},
    ],
    'blocks': [{'type': 'question', 'name': 'Question', 'settings': [t('question', 'Question'), rt('answer', 'Answer')]}],
    'presets': [{'name': 'AR · FAQ', 'blocks': [
        {'type': 'question', 'settings': {'question': 'Is using a digital tasbih counter permissible?', 'answer': '<p>Many scholars regard counting aids such as beads and digital counters as permissible, as long as you don’t believe the tool itself carries any blessing. Counting on the fingers of the right hand is the Sunnah, and many of our customers use their fingers for the adhkar after salah and the ring for larger daily goals. If you’re unsure, ask a scholar you trust.</p>'}},
        {'type': 'question', 'settings': {'question': 'Which finger should I wear it on?', 'answer': '<p>Most people wear it on the index finger so the thumb rests naturally on the button, but it works on any finger. Some scholars advise men not to wear rings on the index or middle finger, based on a hadith in Sahih Muslim. If you follow that view, the ring finger works well and the button is still within easy reach of your thumb.</p>'}},
        {'type': 'question', 'settings': {'question': 'How do I choose my size?', 'answer': '<p>The ring comes in 18mm (about US 8), 20mm (about US 10) and 22mm (about US 12). Most women choose 18mm and most men 20mm. The size guide on the product page shows how to measure. If it doesn’t fit, exchange it free within 60 days.</p>'}},
        {'type': 'question', 'settings': {'question': 'Can I keep it on during wudu?', 'answer': '<p>Yes. It’s IP67 water resistant, so washing your hands and splashes during wudu are fine. Take it off for swimming, hot showers and saunas.</p>'}},
        {'type': 'question', 'settings': {'question': 'How long does the battery last?', 'answer': '<p>3 to 5 days of frequent use on a single charge.</p>'}},
        {'type': 'question', 'settings': {'question': 'Do I need my phone with me?', 'answer': '<p>No. The ring counts and shows your count on its own. Open the Al Rayan app whenever you like to sync your history over Bluetooth and set up prayer-time alerts.</p>'}},
        {'type': 'question', 'settings': {'question': 'Will the vibration be noticeable in meetings?', 'answer': '<p>Only to you. The vibration is a private, silent nudge on your finger. There’s no click and no sound.</p>'}},
        {'type': 'question', 'settings': {'question': 'What if it’s not for me?', 'answer': '<p>You have 60 days to try it. If it doesn’t help you stay consistent, send it back for a full refund. Returns are free from anywhere in the US.</p>'}},
        {'type': 'question', 'settings': {'question': 'Does it make a good gift?', 'answer': '<p>Yes. It’s a thoughtful gift for a parent, a spouse, a friend, or someone who has recently embraced Islam. If you’re guessing the size, they can exchange it free within 60 days.</p>'}},
    ]}]})

# ---------------- final cta ----------------
SECTIONS['ar-final-cta'] = dict(markup=CTA_LIQUID + OPEN.replace('ar ar-section', 'ar ar-section ar-section--tight') + """
  <div class="ar-container">
    <div class="ar-final" data-ar-reveal>
      <div class="ar-media">
        {%- render 'ar-image', image: section.settings.image, sizes: '(min-width: 850px) 50vw, 100vw', placeholder: 'lifestyle-2' -%}
      </div>
      <div class="ar-final__copy">
        {%- if section.settings.eyebrow != blank -%}<p class="ar-eyebrow">{{ section.settings.eyebrow }}</p>{%- endif -%}
        <h2 class="ar-h2">{{ section.settings.heading }}</h2>
        <div class="ar-lead">{{ section.settings.text }}</div>
        <a class="ar-btn ar-btn--gold" href="{{ cta_url }}">{{ cta_label }}{% render 'ar-icon', name: 'arrow' %}</a>
        """ + ASSURANCE + """
      </div>
    </div>
  </div>
</section>""", schema={
    'name': 'AR · Final call to action', 'tag': 'div',
    'settings': [
        image('image'),
        t('eyebrow', 'Eyebrow', 'Keep your remembrance close'),
        irt('heading', 'Heading', 'Make dhikr part of <em>every</em> day'),
        rt('text', 'Text', '<p>For yourself, or for someone you love: a parent, a spouse, or a friend who is new to Islam.</p>'),
        *CTA_SETTINGS('Shop the Dhikr Ring'), *ASSURANCE_SETTINGS,
        bg('ar--white'), ANCHOR,
    ],
    'presets': [{'name': 'AR · Final call to action'}]})

# ---------------- product main ----------------
SECTIONS['ar-product-main'] = dict(markup="""{%- render 'ar-assets' -%}
{%- liquid
  assign current = product.selected_or_first_available_variant
  assign pid = 'ar-pdp-' | append: section.id
  assign form_id = 'ar-form-' | append: section.id
  assign hidden_names = section.settings.hide_options | downcase | split: ','
  assign size_hints = section.settings.size_hints | split: ','
  assign main_media = current.featured_media | default: product.featured_media
-%}
{% capture nl %}
{% endcapture %}
<section class="ar" id="ar-buy">
  <div class="ar-container ar-pdp" id="{{ pid }}" data-ar-product data-money-format="{{ shop.money_format | escape }}" data-update-url="true">
    <script type="application/json" data-ar-variants>{{ product.variants | json }}</script>

    <div class="ar-gallery" data-ar-gallery>
      <div class="ar-gallery__main">
        {%- if main_media -%}
          <img data-ar-main src="{{ main_media.preview_image | image_url: width: 1400 }}"
            srcset="{{ main_media.preview_image | image_url: width: 600 }} 600w, {{ main_media.preview_image | image_url: width: 900 }} 900w, {{ main_media.preview_image | image_url: width: 1400 }} 1400w"
            sizes="(min-width: 990px) 55vw, 100vw" alt="{{ main_media.alt | default: product.title | escape }}"
            width="1400" height="1400" fetchpriority="high">
        {%- else -%}
          {{ 'product-1' | placeholder_svg_tag: 'ar-ph' }}
        {%- endif -%}
        {%- if section.settings.badge != blank -%}<span class="ar-gallery__badge">{{ section.settings.badge }}</span>{%- endif -%}
        {%- if product.media.size > 1 -%}
          <div class="ar-gallery__nav">
            <button type="button" data-ar-prev aria-label="Previous image">{% render 'ar-icon', name: 'chevron-left' %}</button>
            <button type="button" data-ar-next aria-label="Next image">{% render 'ar-icon', name: 'chevron-right' %}</button>
          </div>
        {%- endif -%}
      </div>
      {%- if product.media.size > 1 -%}
        <div class="ar-gallery__thumbs">
          {%- for media in product.media -%}
            <button type="button" data-ar-thumb data-media-id="{{ media.id }}"
              data-src="{{ media.preview_image | image_url: width: 1400 }}"
              data-srcset="{{ media.preview_image | image_url: width: 600 }} 600w, {{ media.preview_image | image_url: width: 900 }} 900w, {{ media.preview_image | image_url: width: 1400 }} 1400w"
              data-alt="{{ media.alt | default: product.title | escape }}"
              aria-label="Show image {{ forloop.index }}" aria-current="{% if media.id == main_media.id %}true{% else %}false{% endif %}">
              <img src="{{ media.preview_image | image_url: width: 200 }}" alt="" width="200" height="200" loading="lazy">
            </button>
          {%- endfor -%}
        </div>
      {%- endif -%}
      {%- if section.settings.gallery_quote != blank -%}
        <figure class="ar-mini-founder">
          {% render 'ar-icon', name: 'heart' %}
          <div><blockquote>{{ section.settings.gallery_quote }}</blockquote><figcaption><strong>{{ section.settings.gallery_quote_author }}</strong></figcaption></div>
        </figure>
      {%- endif -%}
    </div>

    <div class="ar-buy">
      {%- if section.settings.rating_text != blank -%}
        <a class="ar-rating" href="#reviews" style="text-decoration:none">{% render 'ar-stars' %}<span>{{ section.settings.rating_text }}</span></a>
      {%- endif -%}
      <div>
        <h1 class="ar-buy__title">{{ product.title }}</h1>
        {%- if section.settings.subtitle != blank -%}<p class="ar-buy__sub" style="margin-top:10px">{{ section.settings.subtitle }}</p>{%- endif -%}
      </div>

      <div class="ar-price">
        <span class="ar-price__now" data-ar-price="{{ pid }}">{{ current.price | money }}</span>
        <s class="ar-price__was" data-ar-was="{{ pid }}"{% unless current.compare_at_price > current.price %} hidden{% endunless %}>{{ current.compare_at_price | money }}</s>
        {%- assign saving = current.compare_at_price | minus: current.price -%}
        <span class="ar-price__save" data-ar-save="{{ pid }}" data-template="Save [amount]"{% unless current.compare_at_price > current.price %} hidden{% endunless %}>Save {{ saving | money }}</span>
        {%- if section.settings.price_note != blank -%}<p class="ar-price__note">{{ section.settings.price_note }}</p>{%- endif -%}
      </div>

      <ul class="ar-checklist ar-buy__bullets">
        {%- for i in (1..4) -%}
          {%- assign key = 'bullet_' | append: i -%}
          {%- if section.settings[key] != blank -%}<li>{% render 'ar-icon', name: 'check' %}<span>{{ section.settings[key] }}</span></li>{%- endif -%}
        {%- endfor -%}
      </ul>

      {%- form 'product', product, id: form_id, class: 'ar-buy', novalidate: 'novalidate' -%}
        <input type="hidden" name="id" value="{{ current.id }}" data-ar-variant-id>
        {%- unless product.has_only_default_variant -%}
          {%- for option in product.options_with_values -%}
            {%- liquid
              assign oname = option.name | downcase | strip
              assign is_hidden = false
              for h in hidden_names
                assign hs = h | strip
                if hs == oname
                  assign is_hidden = true
                endif
              endfor
              assign is_color = false
              if oname contains 'color' or oname contains 'colour'
                assign is_color = true
              endif
              assign is_size = false
              if oname contains 'size'
                assign is_size = true
              endif
            -%}
            {%- if is_hidden -%}
              <div data-ar-option hidden><input type="hidden" value="{{ option.selected_value | escape }}"></div>
            {%- else -%}
              <fieldset class="ar-opt" data-ar-option>
                <legend><strong>{{ option.name }}:</strong> <span data-ar-selected>{{ option.selected_value }}</span>
                  {%- if is_size and section.settings.show_size_guide -%}
                    <button type="button" data-ar-open="ar-size-{{ section.id }}">{% render 'ar-icon', name: 'ruler' %}Size guide</button>
                  {%- endif -%}
                </legend>
                <div class="ar-opt__values">
                  {%- for value in option.values -%}
                    {%- liquid
                      assign vname = value | append: ''
                      assign vid = form_id | append: '-' | append: option.position | append: '-' | append: forloop.index
                      assign hint = ''
                      for pair in size_hints
                        assign kv = pair | split: '='
                        assign k = kv.first | strip
                        if k == vname
                          assign hint = kv.last | strip
                        endif
                      endfor
                      assign vh = vname | handleize
                      assign swatch = '#D9D4C7'
                      if value.swatch.color
                        assign swatch = value.swatch.color
                      elsif vh contains 'black'
                        assign swatch = '#1B1D1C'
                      elsif vh contains 'rose'
                        assign swatch = '#D4A28C'
                      elsif vh contains 'gold'
                        assign swatch = '#C9A455'
                      elsif vh contains 'silver' or vh contains 'steel'
                        assign swatch = '#C7CBD0'
                      elsif vh contains 'white'
                        assign swatch = '#F4F2EE'
                      endif
                    -%}
                    <input type="radio" id="{{ vid }}" name="ar-{{ section.id }}-{{ option.position }}" value="{{ vname | escape }}"{% if vname == option.selected_value %} checked{% endif %}>
                    <label for="{{ vid }}" class="ar-opt__btn{% if is_color %} ar-swatch{% endif %}">
                      {%- if is_color -%}<i style="--sw: {{ swatch }}"></i>{%- endif -%}
                      <span>{{ vname }}{% if hint != blank %}<small>{{ hint }}</small>{% endif %}</span>
                    </label>
                  {%- endfor -%}
                </div>
              </fieldset>
            {%- endif -%}
          {%- endfor -%}
        {%- endunless -%}

        <div class="ar-buy__actions" id="ar-actions-{{ section.id }}">
          <button type="submit" name="add" class="ar-btn ar-btn--block" data-ar-atc="{{ pid }}"
            data-available="{{ section.settings.atc_label | escape }}" data-soldout="{{ section.settings.soldout_label | escape }}" data-unavailable="Unavailable"
            {% unless current.available %}disabled{% endunless %}>
            <span data-ar-atc-label>{% if current.available %}{{ section.settings.atc_label }}{% else %}{{ section.settings.soldout_label }}{% endif %}</span>
            <span aria-hidden="true">·</span><span data-ar-price="{{ pid }}">{{ current.price | money }}</span>
          </button>
          {%- if section.settings.show_dynamic_checkout -%}{{ form | payment_button }}{%- endif -%}
          {%- if section.settings.assurance != blank -%}
            <p class="ar-assurance" style="justify-content:center">
              {%- assign parts = section.settings.assurance | split: '·' -%}
              {%- for p in parts -%}<span>{% render 'ar-icon', name: 'check' %}{{ p | strip }}</span>{%- endfor -%}
            </p>
          {%- endif -%}
        </div>
      {%- endform -%}

      <div class="ar-boxes">
        {%- for i in (1..4) -%}
          {%- assign ik = 'box_' | append: i | append: '_icon' -%}
          {%- assign hk = 'box_' | append: i | append: '_title' -%}
          {%- assign tk = 'box_' | append: i | append: '_text' -%}
          {%- if section.settings[hk] != blank -%}
            <div class="ar-box">{% render 'ar-icon', name: section.settings[ik] %}<div><strong>{{ section.settings[hk] }}</strong>{{ section.settings[tk] }}</div></div>
          {%- endif -%}
        {%- endfor -%}
      </div>

      <div class="ar-acc">
        {%- for block in section.blocks -%}
          <details {{ block.shopify_attributes }}>
            <summary>{% render 'ar-icon', name: block.settings.icon %}{{ block.settings.title }}</summary>
            <div class="ar-acc__body">{{ block.settings.content }}</div>
          </details>
        {%- endfor -%}
      </div>

      {%- if section.settings.founder_note != blank -%}
        <div class="ar-mini-founder">""" + MARK + """<div>{{ section.settings.founder_note }}</div></div>
      {%- endif -%}
    </div>
  </div>

  {%- if section.settings.show_size_guide -%}
    <dialog class="ar ar-dialog" id="ar-size-{{ section.id }}" aria-labelledby="ar-size-title-{{ section.id }}">
      <div class="ar-dialog__inner">
        <button type="button" class="ar-dialog__close" data-ar-close aria-label="Close">{% render 'ar-icon', name: 'x' %}</button>
        <p class="ar-eyebrow">Size guide</p>
        <h2 class="ar-h3" id="ar-size-title-{{ section.id }}">{{ section.settings.size_title }}</h2>
        {%- if section.settings.size_image != blank -%}
          <div class="ar-media">{%- render 'ar-image', image: section.settings.size_image, sizes: '560px' -%}</div>
        {%- endif -%}
        <table class="ar-table">
          <thead><tr><th>Size</th><th>Inner diameter</th><th>Circumference</th><th>Approx. US</th></tr></thead>
          <tbody>
            {%- assign rows = section.settings.size_rows | split: nl -%}
            {%- for row in rows -%}
              {%- assign cells = row | split: '|' -%}
              {%- if cells.size > 1 -%}<tr>{% for c in cells %}<td>{{ c | strip }}</td>{% endfor %}</tr>{%- endif -%}
            {%- endfor -%}
          </tbody>
        </table>
        <div class="ar-small">{{ section.settings.size_how }}</div>
      </div>
    </dialog>
  {%- endif -%}

  {%- if section.settings.show_sticky -%}
    <div class="ar ar-sticky" data-ar-sticky data-trigger="ar-actions-{{ section.id }}">
      <div class="ar-sticky__inner">
        <div class="ar-sticky__thumb">
          {%- if product.featured_media -%}<img src="{{ product.featured_media.preview_image | image_url: width: 120 }}" alt="" width="60" height="60" loading="lazy">{%- endif -%}
        </div>
        <div class="ar-sticky__info">
          <strong>{{ product.title }}</strong>
          <span><span data-ar-price="{{ pid }}">{{ current.price | money }}</span><span class="ar-hide-sm"> · <span data-ar-variant-title="{{ pid }}">{{ current.title }}</span></span></span>
        </div>
        <button type="submit" form="{{ form_id }}" class="ar-btn" data-ar-atc="{{ pid }}"
          data-available="{{ section.settings.atc_label | escape }}" data-soldout="{{ section.settings.soldout_label | escape }}" data-unavailable="Unavailable"
          {% unless current.available %}disabled{% endunless %}>
          <span data-ar-atc-label>{% if current.available %}{{ section.settings.atc_label }}{% else %}{{ section.settings.soldout_label }}{% endif %}</span>
        </button>
      </div>
    </div>
  {%- endif -%}
</section>""", schema={
    'name': 'AR · Product', 'tag': 'div', 'enabled_on': {'templates': ['product']},
    'settings': [
        t('rating_text', 'Rating text', '4.9 · 8,200+ wearers'),
        t('subtitle', 'Subtitle', 'The city moves fast. Your remembrance shouldn’t stop.'),
        t('price_note', 'Price note', 'Less than the cost of a monthly gym pass.'),
        t('badge', 'Image badge', 'IP67 · Wudu-safe'),
        header('Highlights'),
        t('bullet_1', 'Highlight 1', 'Silent thumb tap: discreet in meetings and classes'),
        t('bullet_2', 'Highlight 2', 'Gentle vibrations at 33, 66 and 99'),
        t('bullet_3', 'Highlight 3', 'Prayer-time alerts for all five daily prayers'),
        t('bullet_4', 'Highlight 4', 'Syncs with the Al Rayan app to track your progress'),
        header('Options'),
        t('hide_options', 'Hide these options', 'Ships From', info='Comma-separated option names to keep out of view (the first value is used).'),
        cb('show_size_guide', 'Show size guide', True),
        t('size_hints', 'Size hints', '18mm=US 8, 20mm=US 10, 22mm=US 12', info='Shown under each size button. Format: value=hint, value=hint'),
        header('Buy buttons'),
        t('atc_label', 'Add to cart label', 'Add to cart'), t('soldout_label', 'Sold out label', 'Sold out'),
        cb('show_dynamic_checkout', 'Show express checkout (Shop Pay, Apple Pay…)', True),
        t('assurance', 'Reassurance line', 'Free US shipping · 60-day money-back guarantee', info='Separate items with ·'),
        cb('show_sticky', 'Show sticky add-to-cart bar', True),
        header('Feature boxes'),
        icon('box_1_icon', 'Box 1 icon', 'volume'), t('box_1_title', 'Box 1 title', 'Silent devotion'), t('box_1_text', 'Box 1 text', 'No clicking sounds in meetings.'),
        icon('box_2_icon', 'Box 2 icon', 'clock'), t('box_2_title', 'Box 2 title', 'Prayer sync'), t('box_2_text', 'Box 2 text', 'A gentle buzz for each prayer.'),
        icon('box_3_icon', 'Box 3 icon', 'drop'), t('box_3_title', 'Box 3 title', 'Wudu-safe'), t('box_3_text', 'Box 3 text', 'IP67 water resistant.'),
        icon('box_4_icon', 'Box 4 icon', 'refresh'), t('box_4_title', 'Box 4 title', 'Never lose count'), t('box_4_text', 'Box 4 text', 'Saved on the ring, up to 99,999.'),
        header('Quote & founder note'),
        ta('gallery_quote', 'Quote under images', '“This ring turned my 40-minute subway commute into the most spiritual part of my day.”'),
        t('gallery_quote_author', 'Quote author', 'Sarah W., New York'),
        rt('founder_note', 'Founder note', '<p><strong>Made by a young Muslim woman.</strong> Al Rayan is a small business built to help Muslims remember Allah throughout their day. Thank you for being part of it.</p>'),
        header('Size guide'),
        t('size_title', 'Title', 'Find your size'),
        image('size_image', 'Size chart image'),
        ta('size_rows', 'Rows', '18mm|18 mm|56.5 mm|8\n20mm|20 mm|62.8 mm|10\n22mm|22 mm|69.1 mm|12', info='One row per line: size|diameter|circumference|US size'),
        rt('size_how', 'How to measure', '<p><strong>How to measure:</strong> wrap a strip of paper around the base of the finger you’ll wear it on, mark where it overlaps and measure the length in mm. That’s your circumference. Between two sizes? Choose the larger one. If it doesn’t fit, exchange it free within 60 days.</p>'),
    ],
    'blocks': [{'type': 'accordion', 'name': 'Accordion row', 'settings': [icon(default='info'), t('title', 'Title'), rt('content', 'Content')]}],
    'presets': [{'name': 'AR · Product', 'blocks': [
        {'type': 'accordion', 'settings': {'icon': 'ring', 'title': 'Specifications', 'content': '<ul><li>Count memory: up to 99,999</li><li>Display: OLED</li><li>Water resistance: IP67</li><li>Battery: 3–5 days of frequent use</li><li>Vibration at 33, 66 and 99, plus prayer-time alerts</li><li>Bluetooth sync with the Al Rayan app</li><li>Sizes: 18mm, 20mm, 22mm</li><li>Finish: alloy</li></ul>'}},
        {'type': 'accordion', 'settings': {'icon': 'book', 'title': 'Getting started', 'content': '<p>Charge the ring fully before first use. Press the side button once for each recitation; the screen shows your running count and the ring vibrates at 33, 66 and 99. Pair it with the Al Rayan app to set prayer-time alerts and see your history.</p>'}},
        {'type': 'accordion', 'settings': {'icon': 'truck', 'title': 'Shipping & returns', 'content': '<p>Free shipping on every US order, with tracking. You have 60 days to try the ring: if it isn’t right for you, return it free from anywhere in the US for a full refund or a different size.</p>'}},
        {'type': 'accordion', 'settings': {'icon': 'shield', 'title': 'Warranty', 'content': '<p>Every ring is covered by a one-year tech warranty. If something stops working, message us and we’ll make it right.</p>'}},
    ]}]})

# ---------------- write ----------------
os.makedirs(f'{ROOT}/sections', exist_ok=True)
for name, s in SECTIONS.items():
    body = s['markup'].strip() + '\n\n{% schema %}\n' + json.dumps(s['schema'], indent=2, ensure_ascii=False) + '\n{% endschema %}\n'
    open(f'{ROOT}/sections/{name}.liquid', 'w').write(body)


# ---------------- templates (prefilled with the store's existing images) ----------------
def section_entry(name, settings=None, block_images=None):
    sch = SECTIONS[name]['schema']
    entry = {'type': name, 'settings': {}}
    for s in sch.get('settings', []):
        if 'id' in s and 'default' in s:
            entry['settings'][s['id']] = s['default']
    entry['settings'].update(settings or {})
    preset = sch['presets'][0]
    if preset.get('blocks'):
        entry['blocks'], entry['block_order'] = {}, []
        for i, b in enumerate(preset['blocks']):
            bid = f'{b["type"]}_{i + 1}'
            bs = dict(b['settings'])
            if block_images and i < len(block_images) and block_images[i]:
                bs['image'] = img(block_images[i])
            entry['blocks'][bid] = {'type': b['type'], 'settings': bs}
            entry['block_order'].append(bid)
    return entry


def template(order):
    secs, ids = {}, []
    for key, entry in order:
        secs[key] = entry; ids.append(key)
    return {'sections': secs, 'order': ids}


REVIEW_PHOTOS = ['forge-img-sync-5-1790365558437.jpg', 'S2656b29b90fa48b785c537ba67b91ea1W.webp',
                 'S75b9f2d098494937abff1564973bf83bJ.webp', 'S6b6929f098f44d098a1d5aa3ebe256d2A.webp',
                 'Screenshot_2026-09-25_at_4.20.47_PM.png', 'S8193927441f54904b764f762d659135aI.webp']

home = template([
    ('hero', section_entry('ar-hero', {'product': PRODUCT_HANDLE, 'image': img('forge-deploy-9-1790365411277.jpg'), 'secondary_link': '#moments'})),
    ('trust', section_entry('ar-trust-bar')),
    ('intention', section_entry('ar-intention', {'link': '#moments'})),
    ('moments', section_entry('ar-moments', {'anchor_id': 'moments'}, ['forge-deploy-11-1790365412593.jpg', 'forge-img-sync-1-1790365552250.jpg', 'forge-img-sync-3-1790365555415.jpg'])),
    ('features', section_entry('ar-features', {'image': img('ADIKRING.png')})),
    ('comparison', section_entry('ar-comparison')),
    ('reviews', section_entry('ar-reviews', {}, REVIEW_PHOTOS)),
    ('founder', section_entry('ar-founder', {'image': img('forge-img-sync-6-1790365560275.jpg')})),
    ('guarantee', section_entry('ar-guarantee', {'product': PRODUCT_HANDLE})),
    ('faq', section_entry('ar-faq', {'link': '/pages/contact'})),
    ('final', section_entry('ar-final-cta', {'product': PRODUCT_HANDLE, 'image': img('forge-img-sync-8-1790365563044.jpg')})),
])
prod = template([
    ('main', section_entry('ar-product-main', {'size_image': img('DIKRINGSIZES.png')})),
    ('trust', section_entry('ar-trust-bar')),
    ('how', section_entry('ar-how', {}, ['forge-img-sync-0-1790365550541.jpg', 'forge-img-sync-1-1790365552250.jpg', 'forge-img-sync-2-1790365553724.jpg'])),
    ('features', section_entry('ar-features', {'image': img('forge-img-sync-3-1790365555415.jpg'), 'background': 'ar--cream'})),
    ('comparison', section_entry('ar-comparison', {'background': 'ar--white'})),
    ('reviews', section_entry('ar-reviews', {'background': 'ar--paper'}, REVIEW_PHOTOS)),
    ('guarantee', section_entry('ar-guarantee')),
    ('faq', section_entry('ar-faq', {'link': '/pages/contact'})),
    ('final', section_entry('ar-final-cta', {'image': img('forge-img-sync-7-1790365562099.jpg')})),
])
os.makedirs(f'{ROOT}/templates', exist_ok=True)
json.dump(home, open(f'{ROOT}/templates/index.json', 'w'), indent=2, ensure_ascii=False)
json.dump(prod, open(f'{ROOT}/templates/product.al-rayan.json', 'w'), indent=2, ensure_ascii=False)
print('sections:', len(SECTIONS))
