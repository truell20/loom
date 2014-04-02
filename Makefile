all: build

build:
	mkdir -p build
	cd build && cmake .. && $(MAKE)

clean: FORCE
	git clean -Xdf

test:
	@pyflakes loom/schema_pb2.py \
	  || (echo '...patching schema_pb2.py' \
	    ; sed -i '/descriptor_pb2/d' loom/schema_pb2.py)  # HACK
	pyflakes setup.py loom
	pep8 --repeat --ignore=E265 --exclude=*_pb2.py setup.py loom
	nosetests -v
	@echo '----------------'
	@echo 'PASSED ALL TESTS'

FORCE:
