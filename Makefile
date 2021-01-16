.PHONY = all clean
NAME = anki_libunity
TGT = $(NAME).ankiaddon

all: $(TGT)

$(TGT): $(NAME)/__init__.py $(NAME)/config.json
	zip -j $@ $^

clean:
	rm -rvf $(TGT)