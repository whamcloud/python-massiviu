srpm:
	mkdir -p /tmp/_topdir/SOURCES
	cp -r ./* /tmp/_topdir/SOURCES
	rpmbuild -bs --define "_topdir /tmp/_topdir" python-massiviu.spec
	cp -r /tmp/_topdir/SRPMS/* $(outdir)