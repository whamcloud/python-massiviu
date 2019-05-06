BUILDROOT:=$(shell [ -d "/build" ] && echo "/build" || echo ".")
TMPDIR:=$(shell mktemp -d)

srpm:
	yum install -y python2-devel
	mkdir -p ${TMPDIR}/_topdir/SOURCES
	cp -r ${BUILDROOT}/* ${TMPDIR}/_topdir/SOURCES
	rpmbuild -bs -D "_topdir ${TMPDIR}/_topdir" ${TMPDIR}/_topdir/SOURCES/python-massiviu.spec
	cp -r ${TMPDIR}/_topdir/SRPMS/* $(outdir)
	rm -rf ${TMPDIR}