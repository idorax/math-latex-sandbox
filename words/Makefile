TARGETS = 202409A.json \
          wreader

all: $(TARGETS)

.phony: clean clobber cl

%.json: %.yaml
	imod $<
	yamladm j $< > $@

%: %.py
	cp $< $@
	chmod +x $@

clean:

clobber: clean
	rm -f $(TARGETS)
cl: clobber
