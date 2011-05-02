from django_assets import Bundle, register
js = Bundle('js/script.js', 'js/plugins.js','js/mylibs/tooltips.js','js/mylibs/jquery.ui.potato.menu.js',
             output='gen/packed.js')
register('js_all', js)


bpcss = Bundle('css/style.css',
            filters='cssmin', output='gen/bp_packed.css')
register('css_bp', bpcss)

css = Bundle('css/index.scss','css/profile.scss','css/base.scss', 'css/controls.css','css/login.scss','css/menu.css','css/footer.css','css/tooltips.css','css/dev_tools.css',
            filters='scss, cssmin', output='gen/packed.css')
register('css_all', css)

mcss = Bundle('css/mish.scss','css/base.scss','css/css3buttons.css',
            filters='scss, cssmin', output='gen/mish_packed.css')
register('css_mish', mcss)
