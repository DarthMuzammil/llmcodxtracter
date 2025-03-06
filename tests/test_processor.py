# import pytest
# from src.processor import LLMOutputProcessor, LLMOutputValidator, LLMCodeExtractor
# from src.exceptions import LLMOutputException

# validator = LLMOutputValidator()
# extractor = LLMCodeExtractor()
# processor = LLMOutputProcessor(validator, extractor)

# def test_process_valid_code():
#     text = "```python //script.py print('Test')```"
#     code_block = processor.process(text)
#     assert code_block.filename == "script.py"
#     assert code_block.extension == "python"
#     assert code_block.code == "print('Test')"

# def test_process_invalid_code():
#     text = "Invalid LLM output"
#     with pytest.raises(LLMOutputException):
#         processor.process(text)
