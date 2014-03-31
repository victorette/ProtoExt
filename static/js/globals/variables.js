/*
 *  Variables Globales
 *
 */

_SM = {};

// Estados en cada fila de la grilla al iteractuar con el BackEnd
_SM._ROW_ST = {
    REFONLY   : 'REF_ONLY',
    ERROR     : 'ROWST_ERR',
    NEWROW     : 'ROWST_NEW'
   };

// afterLabelTextTpl: _SM._requiredField,
_SM._requiredField = '<span style="color:red;font-weight:bold" data-qtip="Required">*</span>';

_SM._versionProto = '';
_SM._siteTitle = '<div class="top-piv">'+
    '<div class="menu-piv"></div>'+
    '<div class="piv">'+
        '<div class="logo">'+
            '<img src="http://www.cspq.gouv.qc.ca/images/commun/entete/CSPw3.gif" />'+
        '</div>'+
        '<div class="content">'+
            '<div class="title">'+
                'Portrait du logiciel libre dans l\'administration publique de Québec'+
            '</div>'+
            '<div class="subtitle"></div>'+
        '</div>'+
    '</div>'+
'</div>';

_SM.loginTitle = 'Identification – portrait du logiciel au gouvernement du Québec';
_SM._siteTitleCollapsed = false;
_SM.footerExtraContent = '<div class="centre">' +
	'<div id="pied">'+
		'<div class="confidentialite">'+
			'<a href="http://www.gouv.qc.ca/portail/quebec/pgs/commun/informationsutiles/confidentialite/?lang=fr" target="_Blank">Politique de confidentialit&eacute;</a>'+
		'</div>'+
		'<a href="http://www.gouv.qc.ca" title="Lien vers un autre site. Cliquer sur le bouton droit pour l\'ouvrir dans une nouvelle fenetre." target="_Blank"><img src="protoExt/static/img/quebw1.gif" alt="Signature du gouvernement du Qu&eacute;bec." name="logoqc" width="105" height="32" border="0" id="logoqc"/></a>'+
		'<div class="droits" >'+
			'&copy; <a href="http://www.droitauteur.gouv.qc.ca/copyright.php" target="_Blank">Gouvernement du Qu&eacute;bec, 2014</a>' +
		'</div>'+
	'</div>'+
'</div>';

// Strings and messages moved to locale
_SM.__language = {};

// Config Variables
_SM._PConfig =  {
    urlMenu         : 'protoLib/protoGetMenuData/',
    urlGetPCI         : 'protoLib/protoGetPCI/',
    urlSaveProtoObj         : 'protoLib/protoSaveProtoObj/',
    urlGetFieldTree : 'protoLib/protoGetFieldTree/',
    urlGetDetailsTree : 'protoLib/protoGetDetailsTree/',
    urlGetUserRights : 'protoLib/protoGetUserRights/',
    urlGetPasswordRecovery : 'protoLib/protoGetPasswordRecovery/', 
    urlSubmitChangePassword : 'protoLib/submitChangePassword/',
    urlGetSheetReport : 'protoLib/sheetConfigRep/',
    urlGetProtoCsv : 'protoLib/protoCsv/',
    urlDoAction   : 'protoLib/protoDoActions/',
    urlHelpQbe: 'protoLib/protoGetHelpQbe/',
    urlLogOut:  'protoLib/protoLogout/',
    urlGetNextIncrement: 'protoLib/getFieldIncrement/',

    clsBaseModel: 'ProtoUL.model.'
};

_SM._HELPpath = 'resources/help/index.html';


// Collection of PCL's ( Proto Concept Definition )
_SM._cllPCI = {};


// Define los tipos para el manejo de edicion  (type => xtype)
_SM._gridTypeEditor = {
    'int'   : 'numberfield',
    'float'  : 'numberfield',
    'string' : 'textfield',
    'text'   : 'textarea',
    'date'  : 'datefield',
    'boolean' : 'checkbox'
};

// PageSize par default
_SM._PAGESIZE = 50;

_SM._ComboPageSize = [
                  ['25'],
                  ['50'],
                  ['100'],
                  ['500']
            ];


// Autoload entites
// _SM._AUTOLOAD_PCI = [ 'protoDict.Model', 'protoDict.PropertyModel' ]
_SM._AUTOLOAD_PCI = [ ];
_SM._MENU_COLLAPSED = false ;


_SM._defaultViewIcon = 'default_view';


// Windows Position
_SM._mainWin = null;
_SM._winX = 10;
_SM._winY = 10;


// *  Configuracion del metodo por defecto
// Ext.data.Connection.prototype.method = 'POST';
// Ext.data.Connection.method = 'POST';


_SM.DesignerPanels = {
"tbar" : [{
        "tooltip" : "Update definition",
        "iconCls" : "icon-save",
        "itemId" : "save"
    },{
        "iconCls" : "icon-update",
        "tooltip" : "Redraw",
        "itemId" : "redraw"

    },"-",{
        "tooltip" : "Delete curren node",
        "iconCls" : "icon-nodeDelete",
        "disabled": false,
        "itemId" : "delete"


    },"->",{
        "iconCls" : "icon-error",
        "tooltip" : "Show or hide(clear) error tab",
        "itemId" : "error",
        "hidden" : true,
        "enableToggle" : true,
        "errors" : [],
        "errorCount" : 0,
        "maxErrors" : 60
//    },{
//        "iconCls" : "icon-options",
//        "itemId"  : "options",
//        "tooltip" : "Show options"
//    },{
//        "iconCls" : "icon-help",
//        "itemId"  : "help",
//        "tooltip" : "Show help"
    }
    ],


"toolsTabs" : [{
        "xtype" : "tabpanel",
        "activeTab" : 0,
        "border" : false,
        "defaults": { "layout" : "fit" },
        "items" : [{
            "title" : "Tools",
            "itemId" : "toolsTree",
            "tooltip" : "Design your ui by selecting elements from this tab",
            "layout" : "fit",
            "autoScroll": true
        },
        {
            "title" : "Properties",
            "tooltip" : "Object properties",
            "itemId" : "properties",
            "autoScroll": true,
            "border" : false
        }]
    }],


// ----------------------------------------------------------------------------


"toolsTree" : [
        {
            "text": "Fields",
            "children": []
        }, {

        "text": "Containers",
        "children": [
            {
                "text": "fieldset",
                "qtip": "A Fieldset, containing other form elements",
                "__ptType": "fieldset",
                "children": [],
                "__ptConfig": {
                    "__ptType": "fieldset"
                }
            }, {
                "text": "htmlset",
                "qtip": "A Fieldset, containing HML elements",
                "__ptType": "htmlset",
                "children": [],
                "__ptConfig": {
                    "__ptType": "htmlset"
                }

            }
        ]
    }, {
        "text": "Details",
        "children": []
    }]
};


/* ********   Propiedades comunes
    maxHeight
    minHeight
    Height

    maxWidth
    minWidth
    width
 */


// --------------  Containers

            // }, {
                // "text": "Panel",
                // "qtip": "A simple panel with default layout",
                // "__ptType" : "panel",
                // "children": [],
                // "__ptConfig": {
                    // "layout": "fit",
                    // "xtype": "panel",
                    // "__ptType" : "panel"
                // }
            // }, {
                // "text": "Tab Container",
                // "qtip": "A panel with many tabs",
                // "__ptType": "tabpanel",
                // "children": [],
                // "__ptConfig": {
                    // "__ptType" : "tabpanel",
                    // "layout": "fit",
                    // "title": "",
                    // "activeItem": 0
                // }
            // }, {
                // "text": "Tab Panel",
                // "qtip": "A tab panel",
                // "__ptType": "tab",
                // "children": [],
                // "__ptConfig": {
                    // "__ptType": "tab",
                    // "layout": "fit",
                    // "title": ""
                // }
            // }, {
                // "text": "Accordion Panel",
                // "qtip": "Layout as accordion",
                // "__ptType": "accordion",
                // "children": [],
                // "__ptConfig": {
                    // "__ptType" : "accordion",
                    // "layout": "fit",
                    // "title": "",
                    // "activeItem": 0
                // }
            // }, {
                // "text": "fieldcontainer",
                // "qtip": "A Fieldset, containing field elements",
                // "__ptType": "fieldcontainer",
                // "children": [],
                // "__ptConfig": {
                    // "__ptType": "fieldcontainer"
                    // }


// -----------  Details

    // }, {
        // "text": "Others",
        // "children": [
            // {
                // "text": "Label",
                // "qtip": "A textlabel",
                // "leaf": true,
                // "__ptConfig": {
                    // "xtype": "label",
                    // "text": "Label"
                // }
            // }, {
                // "text": "Button",
                // "qtip": "A button",
                // "leaf": true,
                // "__ptConfig": {
                    // "xtype": "button",
                    // "text": "Ok"
                // }
            // }
        // ]
        
