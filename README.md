# STEMEd+ Professional Development

National professional development for STEM+ educators, with application deadlines in one place, filtered by
your role: **https://stemedplus.github.io/stemed-professional-development/**

- **K-12 teachers** (filter by grade band)
- **Informal educators**: museums, science centers, zoos, aquariums, parks, nature centers, libraries, and
  after-school and outreach programs
- **College and university faculty and instructors**, including lecturers, adjuncts, and two-year college
  faculty (filter by career stage)
- **Graduate students and postdocs** preparing to teach

This site combines the former STEMEd+ Professional Learning (K-12 and informal educators) and STEMEd+ Faculty
Development (college) lists. Their old addresses send visitors here, keeping any filters in old links, and keep
serving copies of this site's calendar and RSS so subscriptions keep working. Short links choose a role:
`#k12`, `#informal`, `#faculty`, `#grad`.

STEMEd+ Professional Development is part of [STEMEd+ Commons](https://stemedplus.hcommons.org/), with
[STEMEd+ Conferences](https://stemedplus.github.io/stemed-conferences/), [STEMEd+ Funding](https://stemedplus.github.io/stemed-funding/),
[STEMEd+ Jobs](https://stemedplus.github.io/stemed-jobs/), the [STEMEd+ Digest](https://stemedplus.github.io/STEMEd-Digest/),
and the [Graduate Programs](https://stemedplus.github.io/stem-ed-research-programs/) list.

## What is listed

- **Who it is for.** The four roles above. Each listing says which roles it is for, plus grade bands for K-12
  programs and career stages for college programs.
- **Who runs it.** Only programs run by a national scholarly or professional society or association (in the US
  or internationally), by a US federal agency (NOAA, NASA, NSF, the National Park Service, the Department of
  Energy, ...), by a national program with federal agency funds (for example, NSF-funded RET Sites or the
  NASA-sponsored GLOBE Program), by the Smithsonian Institution, or by a national private foundation or nonprofit
  (for example, the Knowles Teacher Initiative, The POGIL Project, or the Kern Family Foundation's KEEN workshops).
  The program must be open to people from many schools or institutions. **If we are not sure, we leave it out.**
- **What kinds.** Research and field experiences, fellowships and cohort programs, workshops and institutes,
  online courses, webinar series, mentoring networks, coaching, certificate and certification training, workshops
  brought to your department, and teaching postdocs (such as NIH IRACDA). Teaching-focused job postings are on
  [STEMEd+ Jobs](https://stemedplus.github.io/stemed-jobs/teaching-jobs.html).
- **What it shows.** Who it is for (with grades or career stage), cost or stipend, credit, format, how often it
  runs, and when applications open and close. Programs open for applications are listed first.

### Not included

- **State, regional, and district professional development.** That includes state education agencies, state
  teacher associations and their chapters, regional service centers, district programs, and the state programs
  of national networks (such as state Ag in the Classroom programs or state GLOBE partners' own workshops).
  The page says so at the top, and teachers are pointed to their state agency, state teacher association, or
  district instead.
- **Programs a single campus runs for its own people**, such as a teaching center's workshops or a university's
  own summer institute; and state and regional college programs, such as MAA section NExT programs.
- University courses and degrees, programs run by companies, and programs open only to teachers in one city or state.
- Teaching conferences such as NSTA, NCTM, BCCE, USCOTS, SABER, and the ASEE Annual Conference, which are on
  [STEMEd+ Conferences](https://stemedplus.github.io/stemed-conferences/).

### Considered but not listed

Math for America fellowships (open only to New York City public school teachers) and AMTE programs (for
mathematics teacher educators, not K-12 teachers). The National Effective Teaching Institute (NETI) for engineering faculty: it began as an ASEE program, but its
current workshops are run by its co-directors at host universities, and we could not confirm a society or
national nonprofit sponsor. MAA OPEN Math online workshops: their NSF grant was planned to run through summer 2025,
and we could not confirm 2026 workshops. The Cottrell Scholars Collaborative New Faculty Workshop: we could not
confirm recent offerings.

Disciplines come from the list shared across STEMEd+ Commons, kept in [stemedplus-theme](https://github.com/stemedplus/stemedplus-theme)
(`stemedplus_disciplines.json`). Computer science has its own discipline, Computing, and statistics is listed under Mathematics, as on the other sites.

## Feeds and calendars

| | |
|---|---|
| `feeds/deadlines.ics` | When applications open and close, for Google Calendar, Outlook, or Apple Calendar ("add calendar from URL") |
| `feeds/new.xml` | RSS of newly listed programs |
| `programs.json` | Everything on the site, for reuse |

## Add or correct a listing

- [Suggest a program](https://github.com/stemedplus/stemed-professional-development/issues/new?template=suggest_program.yml)
- [Report new dates or a correction](https://github.com/stemedplus/stemed-professional-development/issues/new?template=update_program.yml)
- No GitHub account? Email the maintainer, Julie Libarkin, at libarkin@msu.edu.

To edit directly, see [CONTRIBUTING.md](CONTRIBUTING.md). Each program is one YAML file in `programs/`,
checked against `schema/program.schema.json`.

## How it works

A GitHub Actions workflow (`.github/workflows/update.yml`) runs every day and on every push:

1. refreshes the shared discipline list from stemedplus-theme;
2. runs the tests and checks every file in `programs/`;
3. builds the site into `output/` and publishes it to GitHub Pages. Sessions whose dates have all passed drop
   off, passed deadlines are marked, programs open for applications move to the top, and the date each program
   was first listed is carried over from the published `programs.json` for the RSS feed.

The footer's "For maintainers" box lists files to re-check: any not checked in 180 days, paused programs not
checked in 60 days, and any session with announced (not yet official) dates within 60 days.

Run it locally:

```sh
pip install -r requirements.txt
python -m unittest discover -s tests -t .
python -m stemed_pd --validate
python -m stemed_pd --out output    # then open output/index.html through a local web server
```

To publish: Settings → Pages → Source: **GitHub Actions**.

## License

Code: MIT ([LICENSE](LICENSE)). Listings in `programs/`: CC BY 4.0 ([programs/LICENSE.md](programs/LICENSE.md)).
