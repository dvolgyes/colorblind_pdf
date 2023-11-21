import os
import pytest
from colorblind_pdf.colorblind_pdf import main


@pytest.fixture
def test_pdf_path():
    return "tests/test.pdf"


def test_process_pdf(test_pdf_path):
    output_dir = "tests/output"
    deficiency_type = "d"
    main(test_pdf_path, output_dir, (deficiency_type,), 150)
    assert os.path.isfile(os.path.join(output_dir, "test_deuteranopia.pdf"))
