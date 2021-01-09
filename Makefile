.PHONY: all $(MAKECMDGOALS)

test-unit:
	pytest --cov --cov-report=xml:results/coverage.xml --cov-report=html:results/coverage --junit-xml=results/unit_result.xml -m unit || true
	junit2html results/unit_result.xml results/unit_result.html

test-api:
	pytest --cov --cov-report=xml:results/coverage.xml --cov-report=html:results/coverage --junit-xml=results/api_result.xml -m api || true
	junit2html results/api_result.xml results/api_result.html
