/* 
 * Basada en  Examples.Ux.statusBar
 * 
 * Modif : 
 *      
 *      showBusy  -->  showBusyI  ( internal )
 *      showBusy ( text ,  clearTemp  ) para autolimpiar el status 
 * 
 * 
 */

Ext.define('ProtoUL.ux.StatusBar', {
    extend: 'Ext.toolbar.Toolbar',
    alternateClassName: 'Ext.ux.StatusBar',
    alias: 'widget.statusbar',
    requires: ['Ext.toolbar.TextItem'],
    cls: 'x-statusbar',
    
    busyIconCls: 'x-status-busy',
    busyText: 'Loading...',
    autoClear: 5000,
    emptyText: '&#160;',
    activeThreadId: 0,
    
    initComponent: function () {
        var right = this.statusAlign === 'right';
        this.callParent(arguments);
        this.currIconCls = this.iconCls || this.defaultIconCls;
        this.statusEl = Ext.create('Ext.toolbar.TextItem', {
            cls: 'x-status-text ' + (this.currIconCls || ''),
            text: this.text || this.defaultText || ''
        });
        if (right) {
            this.cls += ' x-status-right';
            this.add('->');
            this.add(this.statusEl);
        } else {
            this.insert(0, this.statusEl);
            this.insert(1, '->');
        }
    },
    
    setStatus: function (o) {
        var me = this;
        o = o || {};

        var a = me.isLayoutSuspended()

        Ext.suspendLayouts();
        
        if (Ext.isString(o)) {
            o = {
                text: o
            };
        }
        if (o.text !== undefined) {
            me.setText(o.text);
        }
        if (o.iconCls !== undefined) {
            me.setIcon(o.iconCls);
        }
        if (o.clear) {
            var c = o.clear,
                wait = me.autoClear,
                defaults = {
                    useDefaults: true,
                    anim: true
                };
            if (Ext.isObject(c)) {
                c = Ext.applyIf(c, defaults);
                if (c.wait) {
                    wait = c.wait;
                }
            } else if (Ext.isNumber(c)) {
                wait = c;
                c = defaults;
            } else if (Ext.isBoolean(c)) {
                c = defaults;
            }
            c.threadId = this.activeThreadId;
            Ext.defer(me.clearStatus, wait, me, [c]);
        }
        Ext.resumeLayouts(true);
        return me;
    },
    
    clearStatus: function (o) {
        o = o || {};
        var me = this,
            statusEl = me.statusEl;
        if (o.threadId && o.threadId !== me.activeThreadId) {
            return me;
        }
        var text = o.useDefaults ? me.defaultText : me.emptyText,
            iconCls = o.useDefaults ? (me.defaultIconCls ? me.defaultIconCls : '') : '';
        if (o.anim) {
            statusEl.el.puff({
                remove: false,
                useDisplay: true,
                callback: function () {
                    statusEl.el.show();
                    me.setStatus({
                        text: text,
                        iconCls: iconCls
                    });
                }
            });
        } else {
            me.setStatus({
                text: text,
                iconCls: iconCls
            });
        }
        return me;
    },
    
    setText: function (text) {
        var me = this;
        me.activeThreadId++;
        me.text = text || '';
        if (me.rendered) {
            me.statusEl.setText(me.text);
        }
        return me;
    },
    getText: function () {
        return this.text;
    },
    setIcon: function (cls) {
        var me = this;
        me.activeThreadId++;
        cls = cls || '';
        if (me.rendered) {
            if (me.currIconCls) {
                me.statusEl.removeCls(me.currIconCls);
                me.currIconCls = null;
            }
            if (cls.length > 0) {
                me.statusEl.addCls(cls);
                me.currIconCls = cls;
            }
        } else {
            me.currIconCls = cls;
        }
        return me;
    },

    
    showBusyI: function (o) {
        if (Ext.isString(o)) {
            o = {
                text: o
            };
        }
        o = Ext.applyIf(o || {}, {
            text: this.busyText,
            iconCls: this.busyIconCls
        });
        return this.setStatus(o);
    }, 
    
    showBusy: function ( text, clear ) {

        this.showBusyI( text ); 
        
        if( clear ) { 
            Ext.defer(function(){
                this.clearStatus({useDefaults:true});
            }, clear, this);
        }
    }, 

    showError: function ( text   ) {

        this.setStatus({
            text: 'Oops! ' + text ,
            iconCls: 'x-status-error',
            clear: true 
        });

    }, 

    showWarning: function ( text  ) {

        this.setStatus({
            text: text ,
            iconCls: 'x-status-warning',
            clear: true 
        });

    },

    clear: function () {
        // wrapper
        this.clearStatus()
    } 

    
});