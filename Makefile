evaluate: clean
	./eva.py

clean: clean-outputs clean-figs

clean-outputs:
	rm *.{json,csv}

clean-figs:
	rm -rf images/

.PHONY: *
