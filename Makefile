OUTPUT_PATH := Rpi
OS=$(shell uname -s)

.PHONY : all

all:
ifeq ($(OS),Linux)
	sudo python main.py

else
	python main.py

endif

clean:
	find . -name \*pyc -delete

copy: clean
ifeq "$(wildcard $(OUTPUT_PATH))" ""
	mkdir $(OUTPUT_PATH)
	echo "directory not existed"

else
	echo "directory existed"

endif
	cp -R module $(OUTPUT_PATH)
	cp main.py Makefile $(OUTPUT_PATH)


scp:  copy
	scp -r $(OUTPUT_PATH) pi@192.168.0.10:/home/pi
	rm -r $(OUTPUT_PATH)
