# Copyright 2014-2020 Akretion France
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# Copyright 2014 Lorenzo Battistini <lorenzo.battistini@agilebg.com>
# Copyright 2016-2020 Tecnativa - Pedro M. Baeza
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
#                <contact@eficent.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Base Address City Geonames Import",
    "version": "14.0.1.0.0",
    "category": "Partner Management",
    "license": "AGPL-3",
    "summary": "Import zip entries from Geonames",
    "author": (
        "Akretion,"
        "Agile Business Group,"
        "Tecnativa,"
        "AdaptiveCity,"
        "Odoo Community Association (OCA)"
    ),
    "website": "https://github.com/akretion/geonames-import-simple",
    "depends": ["base_address_extended", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_country_data.xml",
        "views/res_country.xml",
        "views/res_city.xml",
        "wizard/geonames_import_view.xml",
    ],
    "installable": True,
}
