compile_report:
	@git submodule update --init --recursive
	@if [ -d 'public/' ] ; then rm -rf public/ ; fi
	@mkdir -p public/css/
	# @pysassc src/scss/main.scss public/css/custom.css
	@rsync -rau static/* public/
	# @pandoc content/*.md templates/references.md --defaults=templates/build.yaml
	@pandoc slides.md --defaults=templates/build.yaml --highlight-style=breezeDark
