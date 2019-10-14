# INGInious-packets

This repository contains the new exercises for the third edition of the open-source [Computer Networking: Principles, Protocols and Practice](http://cnp3book.info.ucl.ac.be) ebook that use Maxime Piraux's [packet dissector](https://github.com/cnp3/INGInious-problems-network-trace) and are hosted on the [INGINIOUS](https://inginious.org) at [https://inginious.org/course/cnp3](https://inginious.org/course/cnp3) 

These exercises are covered by a GPL license.

## Localization

To update the ``.po`` files, make sure to have the ``inginious`` and ``inginious-problems-network-trace`` packages in your Python PATH.

- To generate the ``.pot`` files:

        pybabel extract -F babel.cfg -o \$i18n/messages.pot  .

- To update existing ``.po`` files (replace ``update`` by ``init`` to add a new translation):

        pybabel update -i \$i18n/messages.pot -l {lang} -o \$i18n/{lang}.po

- To compile ``.po`` files:

        pybabel compile -i \$i18n/{lang}.po l {lang} -o \$i18n/{lang}.mo

