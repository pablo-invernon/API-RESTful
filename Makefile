.PHONY: all $(MAKECMDGOALS)

test-unit:
	pytest --cov --cov-report=xml:results/coverage.xml --cov-report=html:results/coverage --junit-xml=results/unit_result.xml -m unit || true
	junit2html results/unit_result.xml results/unit_result.html

test-int:
	pytest --cov --cov-report=xml:results/coverage.xml --cov-report=html:results/coverage --junit-xml=results/int_result.xml -m int || true
	junit2html results/int_result.xml results/int_result.html
