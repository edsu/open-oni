from django.conf.urls.defaults import patterns, url

from chronam import settings
from chronam.settings import STORAGE, STATIC

handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

urlpatterns = patterns(
    'chronam.web.views',

    url(r'^$', 'home', name="chronam_home"),

    url(r'^about/$', 'about', name="chronam_about"),

    url(r'^help/$', 'help', name="chronam_help"),

    # explainOCR.html
    url(r'^about/ocr/$', 'ocr', name="chronam_explain_ocr"),

    # API docs
    url(r'^about/api/$', 'about_api', name="chronam_about_api"),

    # example: /lccn/sn85066387
    url(r'^lccn/(?P<lccn>\w+)/$', 'title', 
        name="chronam_title"),

    # example: /lccn/sn85066387/issues/
    url(r'^lccn/(?P<lccn>\w+)/issues/$', 'issues', name="chronam_issues"),

    # example: /lccn/sn85066387/issues/1900
    url(r'^lccn/(?P<lccn>\w+)/issues/(?P<year>\d{4})/$', 
        'issues', name="chronam_issues_for_year"),

    # example: /lccn/sn85066387/issues/first_pages
    url(r'^lccn/(?P<lccn>\w+)/issues/first_pages/$', 'issues_first_pages', 
        name="chronam_issues_first_pages"),

    # example: /lccn/sn85066387/issues/first_pages/3
    url(r'^lccn/(?P<lccn>\w+)/issues/first_pages/(?P<page_number>\d+)/$', 
        'issues_first_pages', name="chronam_issues_first_pages_page_number"),

    # example: /lccn/sn85066387/marc
    url(r'^lccn/(?P<lccn>\w+)/marc/$', 'title_marc', 
        name="chronam_title_marc"),

    # example: /lccn/sn85066387/feed/
    url(r'^lccn/(?P<lccn>\w+)/feed/$', 'title_atom', 
        name='chronam_title_atom'),

    # example: /lccn/sn85066387/feed/10
    url(r'^lccn/(?P<lccn>\w+)/feed/(?P<page_number>\w+)$', 'title_atom',
        name='chronam_title_atom_page'),

    # example: /lccn/sn85066387/marc.xml
    url(r'^lccn/(?P<lccn>\w+)/marc.xml$', 'title_marcxml',
        name="chronam_title_marcxml"),

    # example: /lccn/sn85066387/holdings
    url(r'^lccn/(?P<lccn>\w+)/holdings/$', 'title_holdings',
        name="chronam_title_holdings"),

    # example: /essays/
    url(r'^essays/$', 'essays', name='chronam_essays'),

    # example: /lccn/sn85066387/essay
    url(r'^lccn/(?P<lccn>\w+)/essays/$', 'title_essays', 
        name="chronam_title_essays"),

    # example: /lccn/sn85066387/essay/20091101091232
    url(r'^lccn/(?P<lccn>\w+)/essays/(?P<created>\d+)/$', 'title_essay',
        name='chronam_title_essay'),

    # example: /lccn/sn85066387/1907-03-17/ed-1
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/$',
        'issue_pages', name="chronam_issue_pages"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/1
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/(?P<page_number>\d+)/$', 
        'issue_pages', name="chronam_issue_pages_page_number"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/$',
        'page', name="chronam_page"),

   # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4.pdf
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+).pdf$',
        'page_pdf', name="chronam_page_pdf"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4.jp2
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+).jp2$',
        'page_jp2', name="chronam_page_jp2"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/ocr.xml
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/ocr.xml$',
        'page_ocr_xml', name="chronam_page_ocr_xml"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/ocr.txt
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/ocr.txt$',
        'page_ocr_txt', name="chronam_page_ocr_txt"),

    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/;words=(?P<words>.+)$',
        'page', name="chronam_page_words"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/coordinates
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/coordinates/$',
        'coordinates', name="chronam_page_coordinates"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/coordinates;words=corn+peas+cigars
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/coordinates/;words=(?P<words>.+)$',
        'coordinates', name="chronam_page_coordinates"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/print/image_813x1024_from_0,0_to_6504,8192
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/print/image_(?P<width>\d+)x(?P<height>\d+)_from_(?P<x1>\d+),(?P<y1>\d+)_to_(?P<x2>\d+),(?P<y2>\d+)/$',
        'page_print', name="chronam_page_print"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/image_813x1024_from_0,0_to_6504,8192.jpg
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/image_(?P<width>\d+)x(?P<height>\d+)_from_(?P<x1>\d+),(?P<y1>\d+)_to_(?P<x2>\d+),(?P<y2>\d+).jpg$',
        'page_image_tile', name="chronam_page_image_tile"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/image_813x1024.jpg
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/image_(?P<width>\d+)x(?P<height>\d+).jpg$',
        'page_image', name="chronam_page_image"),

    # example: /lccn/sn85066387/1907-03-17/ed-1/seq-4/ocr/
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/ocr/$',
        'page_ocr', name="chronam_page_ocr"),

    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)/thumbnail.jpg$',
        'thumbnail', name="chronam_page_thumbnail"),

    url(r'^newspapers/$', 'newspapers', name='chronam_newspapers'),
    url(r'^newspapers/feed/$', 'newspapers_atom', name='chronam_newspapers_atom'),

    url(r'^newspapers.(?P<format>txt)$', 'newspapers', 
        name='chronam_newspapers_format'),

    url(r'^newspapers/(?P<state>[^/;]+)/$', 'newspapers', 
        name='chronam_newspapers_state'),

    url('search/pages/opensearch.xml', 'search_pages_opensearch',
        name='chronam_search_pages_opensearch'),
    url(r'^search/pages/$', 'search_pages', name='chronam_search_pages'),
    url(r'^search/pages/results/$', 'search_pages_results',
        name='chronam_search_pages_results'),
    url(r'^search/pages/results/(?P<view_type>list)/$', 'search_pages_results',
        name='chronam_search_pages_results_list'),

    url('search/titles/opensearch.xml', 'search_titles_opensearch',
        name='chronam_search_titles_opensearch'),
    url(r'^search/titles/$', 'search_titles', 
        name="chronam_search_titles"),
    url(r'^search/titles/results/$', 'search_titles_results', 
        name='chronam_search_titles_results'),

    url(r'^events/$', 'events', name='chronam_events'),
    url(r'^events/feed/$', 'events_atom', name='chronam_events_atom'),
    url(r'^events/(?P<event_id>.+)/$', 'event', name='chronam_event'),
    url(r'^awardees/$', 'awardees', name='chronam_awardees'),

    # example: /titles
    url(r'^titles/$', 'titles', name='chronam_titles'),

    # example: /titles;page=5
    url(r'^titles/;page=(?P<page_number>\d+)$', 'titles', 
            name='chronam_titles_page'),

    # example: /titles;start=F
    url(r'^titles/;start=(?P<start>\w)$', 'titles', name='chronam_titles_start'),

    # example: /titles;start=F;page=5
    url(r'^titles/;start=(?P<start>\w);page=(?P<page_number>\d+)$', 
        'titles', name='chronam_titles_start_page'),

    # example: /titles/places/pennsylvania
    url(r'^titles/places/(?P<state>[^/;]+)/$', 'titles_in_state', 
        name='chronam_state'),

    # example: /titles/places/pennsylvania;page=1
    url(r'^titles/places/(?P<state>[^/;]+)/;page=(?P<page_number>\d+)$',
        'titles_in_state', name='chronam_state_page_number'), 

    # example: /titles/places/pennsylvania;page=1;order=title
    url(r'^titles/places/(?P<state>[^;]+)/;page=(?P<page_number>\d+);(?P<order>\w+)$', 
        'titles_in_state', name='chronam_state_page_number'), 

    # example /titles/places/pennsylvania/allegheny
    url(r'^titles/places/(?P<state>[^/;]+)/(?P<county>[^/;]+)/$', 
        'titles_in_county', name='chronam_county'),

    # example /titles/places/pennsylvania/allegheny;page=1
    url(r'^titles/places/(?P<state>[^/;]+)/(?P<county>[^/;]+)/;page=(?P<page_number>\d+)$', 
        'titles_in_county', name='chronam_county_page_number'),

    # example: /titles/places/pennsylvania/allegheny/pittsburgh
    url(r'^titles/places/(?P<state>[^/;]+)/(?P<county>[^/;]+)/(?P<city>[^/;]+)/$', 
        'titles_in_city', name='chronam_city'),

    # example: /titles/places/pennsylvania/allegheny/pittsburgh;page=1
    url(r'^titles/places/(?P<state>[^/;]+)/(?P<county>[^/]+)/(?P<city>[^/;]+)/;page=(?P<page_number>\d+)$', 
        'titles_in_city', name='chronam_city_page_number'),

    # example: # /titles/places/pennsylvania/allegheny/pittsburgh;page=1;order=title
    url(r'^titles/places/(?P<state>[^/;]+)/(?P<county>[^/;]+)/(?P<city>[^/;]+)/;page=(?P<page_number>\d+);(?P<order>\w+)$', 
        'titles_in_city', name='chronam_city_page_number'),

    # example: /states
    url(r'^states/$', 'states', name='chronam_states'),

    # example: /states_counties/
    url(r'^states_counties/$', 'states_counties', name='chronam_states_counties'),

    # example: /states.json
    url(r'^states.(?P<format>json)$', 'states', name='chronam_states_json'),

    # example: /counties/pennsylvania
    url(r'^counties/(?P<state>[^/;]+)/$', 'counties_in_state', name='chronam_counties_in_state'),

    # example: /counties/pennsylvania.json
    url(r'^counties/(?P<state>[^/;]+).(?P<format>json)$', 'counties_in_state', name='chronam_counties_in_state_json'),

    # example: /cities/pennsylvania/allegheny
    url(r'^cities/(?P<state>[^/;]+)/(?P<county>[^./]+)/$', 'cities_in_county', name='chronam_cities_in_county'),

    # example: /cities/pennsylvania/allegheny.json
    url(r'^cities/(?P<state>[^/;]+)/(?P<county>[^./]+).(?P<format>json)$', 'cities_in_county', name='chronam_cities_in_county_json'),

    # example: /cities/pennsylvania
    url(r'^cities/(?P<state>[^/;]+)/$', 'cities_in_state', name='chronam_cities_in_state'),

    # example: /cities/pennsylvania.json
    url(r'^cities/(?P<state>[^/;]+)\.(?P<format>json)$', 'cities_in_state', name='chronam_cities_in_county_json'),

    # example: /institutions
    url(r'^institutions/$', 'institutions', name='chronam_institutions'),

    # example: /institutions;page=5
    url(r'^institutions/;page=(?P<page_number>\d+)$', 'institutions', 
        name='chronam_institutions_page_number'),

    # example: /institutions/cuy
    url(r'^institutions/(?P<code>[^/]+)/$', 'institution',
        name='chronam_institution'),

    # example: /institutions/cuy/titles
    url(r'^institutions/(?P<code>[^/]+)/titles/$', 'institution_titles',
        name='chronam_institution_titles'),

    # example: /institutions/cuy/titles/5/
    url(r'^institutions/(?P<code>[^/]+)/titles/(?P<page_number>\d+)/$', 
        'institution_titles', name='chronam_institution_titles_page_number'),

    # awardee
    url(r'^awardees/(?P<institution_code>\w+)/$', 'awardee', 
        name='chronam_awardee'),

    url(r'^status', 'status', name='chronam_stats'),
)

# linked-data rdf views

urlpatterns += patterns(
    'chronam.web.views',

    # newspapers
    url(r'^newspapers.rdf$', 'newspapers_rdf', name="chronam_newspapers_dot_rdf"),
    url(r'^newspapers$', 'newspapers_rdf', name="chronam_newspapers_rdf"),

    # title
    url(r'^lccn/(?P<lccn>\w+).rdf$', 'title_rdf', name='chronam_title_dot_rdf'),
    url(r'^lccn/(?P<lccn>\w+)$', 'title_rdf', name='chronam_title_rdf'),

    # issue
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+).rdf$', 'issue_pages_rdf', name='chronam_issue_pages_dot_rdf'),
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)$', 'issue_pages_rdf', name='chronam_issue_pages_rdf'),

    # page
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+).rdf$', 'page_rdf', name="chronam_page_dot_rdf"),
    url(r'^lccn/(?P<lccn>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/ed-(?P<edition>\d+)/seq-(?P<sequence>\d+)$', 'page_rdf', name="chronam_page_rdf"),

    # awardee
    url(r'^awardees/(?P<institution_code>\w+).rdf$', 'awardee_rdf', name='chronam_awardee_dot_rdf'),
    url(r'^awardees/(?P<institution_code>\w+)$', 'awardee_rdf', name='chronam_awardee_rdf'),

    # ndnp vocabulary
    url(r'^terms/.*$', 'terms', name='chronam_terms'),

    # flickr report
    url(r'^flickr/$', 'pages_on_flickr', name='chronam_pages_on_flickr'),

    # batch summary
    url(r'^batches/summary/$', 'batch_summary', name='chronam_batch_summary'),
    url(r'^batches/summary.(?P<format>txt)$', 'batch_summary', 
        name='chronam_batch_summary_txt'),

    # batch view
    url(r'^batches/$', 'batches', name='chronam_batches'),
    url(r'^batches/feed/$', 'batches_atom', name='chronam_batches_atom'),
    url(r'^batches/json/$', 'batches_json', name='chronam_batches_json'),
    url(r'^batches/(?P<batch_name>.+)/$', 'batch', name='chronam_batch'),
    url(r'^batches/(?P<batch_name>.+).rdf$', 'batch_rdf', 
        name='chronam_batch_dot_rdf'),
    url(r'^batches/(?P<batch_name>.+)/json$', 'batch_json', 
        name='chronam_batch_dot_json'),
    url(r'^batches/(?P<batch_name>.+)$', 'batch_rdf', name='chronam_batch_rdf'),

    # reels 
    url(r'^reels/$', 'reels', name='chronam_reels'),
    url(r'^reel/(?P<reel_number>\w+)/$', 'reel', name='chronam_reel'),
)

# these are static files that will normally be served up by apache
# in production deployments before django ever sees the request
# but are useful when running in development environments

urlpatterns += patterns(
    '',

    url(r'^data/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': STORAGE}, name="chronam_batch_files"),

    url(r'^(?P<path>images/.*)$', 'django.views.static.serve', 
        {'document_root': STATIC}, name="chronam_images"),

    url(r'^(?P<path>css/.*)$', 'django.views.static.serve', 
        {'document_root': STATIC}, name="chronam_css"),

    url(r'^(?P<path>javascript/.*)$', 'django.views.static.serve', 
        {'document_root': STATIC}, name="chronam_javascript"),
)