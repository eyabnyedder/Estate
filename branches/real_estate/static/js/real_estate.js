odoo.define('real_estate.reModel', function (require) {
    'use strict';

    var core = require('web.core');
    var FormController = require('web.FormController');
    var Dialog = require('web.Dialog');

    var _t = core._t;

    FormController.include({
        /**
         * Handle the button click event for the "Open Choose Form Wizard" button.
         *
         * @private
         * @param {jQuery.Event} ev
         */
        _onButtonOpenChooseFormWizard: function (ev) {
            ev.stopPropagation();
            ev.preventDefault();

            var self = this;
            var options = {
                title: _t("Choose Form"),
                size: 'medium',
                buttons: [
                    {
                        text: _t("Create Partner"),
                        classes: 'btn-primary',
                        close: true,
                        click: function () {
                            self._createFormView('partner');
                        },
                    },
                    {
                        text: _t("Create Agent"),
                        classes: 'btn-primary',
                        close: true,
                        click: function () {
                            self._createFormView('agent');
                        },
                    },
                ],
            };

            Dialog.alert(null, _t("What would you like to create?"), options);
        },

        /**
         * Create the form view based on the selected form view type.
         *
         * @private
         * @param {string} formViewType - The selected form view type ('partner' or 'agent').
         */
        _createFormView: function (formViewType) {
            var self = this;
            var model = this.modelName;
            var context = this.renderer.state.getContext();
            context['form_view_type'] = formViewType;

            this._rpc({
                model: 'choose.form.wizard',
                method: 'open_form_view',
                args: [],
                context: context,
            }).then(function (result) {
                self.trigger_up('reload');
            });
        },
    });

    return {
        FormController: FormController,
    };
});