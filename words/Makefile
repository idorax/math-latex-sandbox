TARGETS = 202409A.json

all: $(TARGETS)

.phony: clean clobber cl

%.json: %.yaml
	imod $<
	yamladm j $< > $@

clean:

clobber: clean
	rm -f $(TARGETS)
cl: clobber
