TARGETS = 202409.json

all: $(TARGETS)

.phony: clean clobber cl

%.json: %.yaml
	imod $<
	yamladm j $< > $@

clean:

clobber: clean
	rm -f $(TARGETS)
cl: clobber
