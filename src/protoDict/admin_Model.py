# -*- coding: utf-8 -*-

#El modelo tendra dos campos para seleccionar fichas, pues hay un nivel de ficha a nivel de modelo que no
#coincide con el selector usado a nivel de elementods de datos ( properties )
#
#Categoria,       Modelo  
#SubCategoria     Para los elmentos de datos 

from models import *

import django.contrib.admin          
 

class Model_Admin(django.contrib.admin.ModelAdmin):
    
    protoExt = {
    "protoOption": "protoDict.Model",
    "description": "Description des vues",
    "protoConcept": "protoDict.Model",
    "protoIcon": "icon-model",
    "shortTitle": "Vues",
    "version": "121030",
    "helpPath": "",
    "idProperty": "id",
    "sheetConfig": {
        "protoSheetSelector": "udp__Categorie",
        "protoSheets": [
            {
                "name": "DEFAULT",
                "template": "<table class=\"ficha\" cellpadding=\"3\"><tr class=\"azul\"><td class=\"negro\">Nom de la vue: </td><td>{{code}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Catégorie: </td><td>{{category}}</td></tr><tr class=\"azul\"><td class=\"negro\">Auteur de la vue:</td><td>{{udp__Auteurmodele}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Version de la vue: </td><td>{{udp__Version}}</td></tr><tr class=\"azul\"><td class=\"negro\">Document de réréfence: </td><td class=\"desc\">{{udp__docureference}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Description: </td><td>{{udp__Descriptionmodele}}</td></tr></table>",
                "title": "Fiche descriptive des vues corporatives"
            },
            {
                "name": "AT",
                "template": "<table class=\"ficha\" cellpadding=\"3\"><tr class=\"azul\"><td class=\"negro\">Nom de l\'élément de donnée: </td><td>{{code}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Description: </td><td class=\"desc\">{{description}}</td></tr><tr class=\"azul\"><td class=\"negro\">Statut élément de donnée:</td><td class=\"desc\">{{udp__STATUTELEMENTDEDONNEE}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Acteur principal: </td><td class=\"desc\">{{udp__ActeurPrincipal}}</td></tr><tr class=\"azul\"><td class=\"negro\">Autres acteurs: </td><td>{{udp__AutresActeurs}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Intrants déclencheurs: </td><td class=\"desc\">{{udp__IntrantsDeclencheurs}}</td></tr></table>",
                "title": "Fiche descriptive des actions terraines"
            },
            {
                "name": "locale",
                "template": "<table class=\"ficha\" cellpadding=\"3\"><tr class=\"azul\"><td class=\"negro\">Nom de la vue: </td><td>{{code}}</td></tr><tr class=\"azul\"><td class=\"negro\">Catégorie: </td><td>{{udp__Categorie}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Sous-Catégorie:</td><td>{{udp__Souscategorie}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Auteur de la vue:</td><td>{{udp__Auteurmodele}}</td></tr><tr class=\"azul\"><td class=\"negro\">Version de la vue: </td><td>{{udp__Version}}</td></tr><tr class=\"blanco\"><td class=\"negro\">Description: </td><td class=\"desc\">{{udp__Descriptionmodele}}</td></tr></table>",
                "title": "Fiche descriptive des vues locales"
            }
        ],
        "protoSheetProperties": [
            "code",
            "udp__Souscategorie",
            "udp__Auteurmodele",
            "udp__Version",
            "udp__Descriptionmodele",
            "udp__ActeurPrincipal",
            "udp__AutresActeurs",
            "udp__IntrantsDeclencheurs",
            "category",
            "udp__docureference"
        ]
    },
    "gridConfig": {
        "hideRowNumbers": False,
        "filterSetABC": "",
        "hiddenFields": [],
        "listDisplay": [
            "code",
            "udp__Descriptionmodele"
        ],
        "baseFilter": {},
        "initialFilter": {},
        "filtersSet": [
            {
                "filter": {
                    "code__istartswith": "AT"
                },
                "name": "Vue AT"
            },
            {
                "filter": {
                    "code__istartswith": "Vue Corporative"
                },
                "name": "Vue corportative"
            },
            {
                "filter": {
                    "code__istartswith": "Vue locale"
                },
                "name": "Vue locale"
            },
            {
                "filter": {},
                "name": " Tous "
            }
        ],
        "readOnlyFields": [],
        "sortFields": [
            "code"
        ],
        "initialSort": [
            {
                "direction": "ASC",
                "property": "code"
            }
        ],
        "searchFields": [
            "code"
        ]
    },
    "fields": [
        {
            "flex": 1,
            "fieldLabel": "Nom de la vue",
            "allowBlank": False,
            "width": 200,
            "tooltip": "",
            "header": "Nom de la vue",
            "fromModel": True,
            "type": "string",
            "name": "code"
        },
        {
            "header": "Catégorie",
            "type": "string",
            "name": "udp__Categorie",
            "flex": 1,
            "checked": True
        },
        {
            "flex": 1,
            "fieldLabel": "Modèle",
            "name": "__str__",
            "fkId": "id",
            "zoomModel": "protoDict.Model",
            "cellLink": True,
            "header": "ModèLe",
            "readOnly": True,
            "type": "string",
            "allowBlank": True
        },
        {
            "flex": 1,
            "checked": True,
            "name": "udp__ActeurPrincipal",
            "header": "Acteur principal",
            "wordWrap": True,
            "type": "text"
        },
        {
            "header": "Version",
            "type": "string",
            "name": "udp__Version",
            "flex": 1,
            "checked": True
        },
        {
            "header": "Sous-Catégorie",
            "type": "string",
            "name": "udp__Souscategorie",
            "flex": 0.5,
            "checked": True
        },
        {
            "flex": 6,
            "vType": "htmlText",
            "fieldLabel": "Description",
            "name": "udp__Descriptionmodele",
            "header": "Description",
            "checked": True,
            "type": "text"
        },
        {
            "fieldLabel": "Catégorie",
            "name": "category",
            "width": 100,
            "header": "Catégorie",
            "fromModel": True,
            "type": "string"
        },
        {
            "flex": 1,
            "checked": True,
            "name": "udp__AutresActeurs",
            "header": "Autres acteurs",
            "cellToolTip": True,
            "type": "text"
        },
        {
            "flex": 1,
            "checked": True,
            "name": "udp__IntrantsDeclencheurs",
            "header": "Intrants déclencheurs",
            "wordWrap": True,
            "type": "text"
        },
        {
            "header": "Auteur",
            "type": "string",
            "name": "udp__Auteurmodele",
            "flex": 1,
            "checked": True
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__nomsibdm",
            "readOnly": False,
            "type": "udp",
            "name": "udp__nomsibdm"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__acronyme",
            "readOnly": False,
            "type": "udp",
            "name": "udp__acronyme"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__uniteadministrative",
            "readOnly": False,
            "type": "udp",
            "name": "udp__uniteadministrative"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__datecn",
            "readOnly": False,
            "type": "udp",
            "name": "udp__datecn"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__nomrealisateurcn",
            "readOnly": False,
            "type": "udp",
            "name": "udp__nomrealisateurcn"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__nomredacteurs",
            "readOnly": False,
            "type": "udp",
            "name": "udp__nomredacteurs"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__nomsecretariat",
            "readOnly": False,
            "type": "udp",
            "name": "udp__nomsecretariat"
        },
        {
            "checked": True,
            "allowBlank": True,
            "header": "udp__docureference",
            "readOnly": False,
            "type": "udp",
            "name": "udp__docureference"
        },
        {
            "fkField": "domain",
            "zoomModel": "protoDict.Domain",
            "name": "domain_id",
            "header": "domain_id",
            "readOnly": True,
            "type": "foreignid",
            "allowBlank": False
        },
        {
            "zoomModel": "protoDict.Domain",
            "name": "domain",
            "fkId": "domain_id",
            "cellLink": True,
            "header": "Domaine",
            "readOnly": False,
            "type": "foreigntext",
            "allowBlank": False
        }
    ],
    "protoUdp": {
        "propertyPrefix": "udp",
        "propertyReference": "model",
        "propertyRef": "model",
        "propertyName": "code",
        "propertyValue": "valueUdp",
        "keyField": "",
        "udpTable": "udpModel"
    },
    "protoDetails": [
        {
            "detailTitleLbl": "Vue :",
            "conceptDetail": "protoDict.Concept",
            "detailField": "model__pk",
            "masterTitleField": "code",
            "menuText": "Entité",
            "masterField": "pk"
        },
        {
            "detailTitleLbl": " ",
            "detailField": "model__pk",
            "conceptDetail": "protoDict.PropertyModel",
            "masterTitleField": "code",
            "menuText": "Éléments de Données",
            "masterField": "pk"
        },
        {
            "menuText": "Propriétés ",
            "conceptDetail": "protoDict.UdpModel",
            "detailField": "model__pk",
            "masterField": "pk"
        }
    ],
    "protoForm": {
        "__ptType": "protoForm",
        "title": "",
        "items": [
            {
                "fsLayout": "1col",
                "__ptType": "fieldset",
                "title": "Informations d\'ordre général",
                "items": [
                    {
                        "zoomModel": "protoDict.Domain",
                        "fieldLabel": "Domaine",
                        "xtype": "protoZoom",
                        "fkId": "domain_id",
                        "editable": False,
                        "__ptType": "formField",
                        "name": "domain",
                        "readOnly": False,
                        "hidden": "true",
                        "allowBlank": False
                    },
                    {
                        "name": "code",
                        "fieldLabel": "Nom de la vue",
                        "allowBlank": False,
                        "__ptType": "formField",
                        "xtype": "textfield"
                    },
                    {
                        "tooltip": "CN, AT ou défault",
                        "fieldLabel": "Catégorie",
                        "xtype": "textfield",
                        "__ptType": "formField",
                        "name": "category"
                    },
                    {
                        "fieldLabel": "Sous-Catégorie",
                        "xtype": "textfield",
                        "tooltip": "Le nom du modélisateur de la vue",
                        "__ptType": "formField",
                        "hidden": "true",
                        "name": "udp__Souscategorie"
                    },
                    {
                        "tooltip": "Le nom du créateur de la vue",
                        "fieldLabel": "Auteur de la vue",
                        "xtype": "textfield",
                        "__ptType": "formField",
                        "name": "udp__Auteurmodele"
                    },
                    {
                        "tooltip": "Numéro de version de la vue",
                        "fieldLabel": "Version",
                        "xtype": "textfield",
                        "__ptType": "formField",
                        "name": "udp__Version"
                    },
                    {
                        "fieldLabel": "Document de référence",
                        "allowBlank": True,
                        "__ptType": "formField",
                        "name": "udp__docureference",
                        "readOnly": False,
                        "tooltip": "Type de document utilisé pour créer la vue",
                        "xtype": "textfield"
                    },
                    {
                        "__ptType": "htmlset",
                        "items": [
                            {
                                "fieldLabel": "Description",
                                "xtype": "textarea",
                                "name": "udp__Descriptionmodele",
                                "__ptType": "formField",
                                "height": 100,
                                "labelAlign": "top"
                            }
                        ]
                    }
                ]
            },
            {
                "fsLayout": "1col",
                "__ptType": "fieldset",
                "title": "Informations concernant le Cadre Normatif",
                "items": [
                    {
                        "fieldLabel": "Nom du système d\'information ou de la banque de données ministérielle",
                        "xtype": "textfield",
                        "__ptType": "formField",
                        "width": 510,
                        "readOnly": False,
                        "allowBlank": True,
                        "name": "udp__nomsibdm"
                    },
                    {
                        "fieldLabel": "Acronyme SI ou BDM",
                        "allowBlank": True,
                        "__ptType": "formField",
                        "name": "udp__acronyme",
                        "readOnly": False,
                        "xtype": "textfield"
                    },
                    {
                        "fieldLabel": "Nom unité administrative",
                        "allowBlank": True,
                        "__ptType": "formField",
                        "name": "udp__uniteadministrative",
                        "readOnly": False,
                        "xtype": "textfield"
                    },
                    {
                        "fieldLabel": "Date du Cadre Normatif",
                        "xtype": "datefield",
                        "__ptType": "formField",
                        "readOnly": False,
                        "allowBlank": True,
                        "type": "date",
                        "name": "udp__datecn"
                    },
                    {
                        "fieldLabel": "Nom du réalisateur",
                        "allowBlank": True,
                        "__ptType": "formField",
                        "name": "udp__nomrealisateurcn",
                        "readOnly": False,
                        "xtype": "textfield"
                    },
                    {
                        "fieldLabel": "Nom(s) des rédacteurs",
                        "allowBlank": True,
                        "__ptType": "formField",
                        "name": "udp__nomredacteurs",
                        "readOnly": False,
                        "xtype": "textfield"
                    },
                    {
                        "fieldLabel": "Nom(s) secrétariat",
                        "allowBlank": True,
                        "__ptType": "formField",
                        "name": "udp__nomsecretariat",
                        "readOnly": False,
                        "xtype": "textfield"
                    }
                ]
            },
            {
                "fsLayout": "1col",
                "__ptType": "fieldset",
                "title": "Informations concernant les AT",
                "items": [
                    {
                        "fieldLabel": "Acteur principal",
                        "xtype": "textarea",
                        "name": "udp__ActeurPrincipal",
                        "__ptType": "formField",
                        "height": 100,
                        "labelAlign": "top"
                    },
                    {
                        "fieldLabel": "Autres acteurs",
                        "xtype": "textarea",
                        "name": "udp__AutresActeurs",
                        "__ptType": "formField",
                        "height": 100,
                        "labelAlign": "top"
                    },
                    {
                        "fieldLabel": "Intrants déclencheurs",
                        "xtype": "textarea",
                        "name": "udp__IntrantsDeclencheurs",
                        "__ptType": "formField",
                        "height": 100,
                        "labelAlign": "top"
                    }
                ]
            }
        ]
    }
}