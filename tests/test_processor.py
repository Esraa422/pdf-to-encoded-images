from pdf_encoder.processor import process_pdf


def test_process_pdf_basic():
    result = process_pdf("examples/Home_Task.pdf")

    assert result["page_count"] > 0
    assert isinstance(result["images"], list)
    assert "total_size_bytes" in result