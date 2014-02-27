/**
 * 
 * @author Dario Gomez 
 * http://

 */

// Ext.require('Ext.toolbar.Paging');
// Ext.require('Ext.layout.container.Border');

//borrar el body:  ( para quitar la mascara ) 
//document.getElementById('Idbody').innerHTML = "";

Ext.Loader.setConfig({enabled: true});
// Ext.Loader.setPath('Ext.ux', 'static/extjs/examples/ux');

Ext.application({
    name: 'ProtoUL',
    appFolder: 'static/js',

    requires: [
        'Ext.window.MessageBox',
        'Ext.toolbar.Paging', 
        'Ext.layout.container.Border',
        
        'Ext.util.Cookies', 
        'Ext.Ajax',
        
        'ProtoUL.view.MenuTree', 
        'ProtoUL.view.ProtoTabContainer',  
        'ProtoUL.view.Viewport',
        'ProtoUL.view.password.PasswordReset',

        'ProtoUL.ux.Printer',
        'ProtoUL.ux.GridHeaderToolTip', 
        'ProtoUL.ux.CheckColumn' 
    ],

	controllers: ['PasswordManager'],
	
    launch: function () {

        // Add csrf token to every ajax request
        var token = Ext.util.Cookies.get('csrftoken');
        if(!token) {
            Ext.Error.raise("Missing csrftoken cookie");
        } else {
            Ext.Ajax.defaultHeaders = Ext.apply(Ext.Ajax.defaultHeaders || {}, {
                'X-CSRFToken' : token
            });
        }

        // 
        Ext.QuickTips.init();
        
        if (window.isPasswordReseted === 'True') {
			this.showResetPasswordForm();
        } else {
        	this.showLogin();
        }
        
    }, 
    showLogin: function(  ) {

        var me = this;

        var options = {
            scope: me, 
            success: function ( obj, result, request ) {
                myWin.hide();
                
                // Globally changing the text of Cancel and Save buttons;
                Ext.grid.RowEditor.prototype.saveBtnText = _SM.__language.Text_Save_Button;
                Ext.grid.RowEditor.prototype.cancelBtnText = _SM.__language.Text_Cancel_Button;
                
                var app = new ProtoUL.view.Viewport();
                
                Ext.destroy( Ext.ComponentQuery.query('protoLogin') );    

            }
        };
        
        var myWin  = Ext.widget('window', {
            constrain: true, 
            iconCls: 'st-user-who',
            title: 'ART - Identification',
            layout: 'fit',
            
            width: 450,
            height: 135,
            
            modal: true,
            items: [ { xtype: 'protoLogin', options : options  }]
        });
        
        myWin.show();
    },
    
    showResetPasswordForm: function() {
    	var resetForm = Ext.create('ProtoUL.view.password.PasswordReset');
        resetForm.show();
    }
    
});