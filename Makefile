all: cffi_grass/grasslib.so

cffi_grass/grasslib.so: cffi_grass/build_grass.py
	python $<

clean:
	rm cffi_grass/*.c cffi_grass/*.o cffi_grass/*.so
