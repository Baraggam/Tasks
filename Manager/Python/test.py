import input_handler
import manager

def testSetMoment():
	resource = manager.Resource()
	resource.setAmount(10000)
	resource.setBegin(60*60)
	resource.setEnd(60*60+5)
	out = resource.setMoment(0, 5)
	assert out == [60*60, 0, 60*60 + 5 , 0]

def test_load_file():
	data = input_handler.load_from_line("test.yaml")
	assert data["ram"] == 0
	assert data["inicio"] == "00:00:00"
	assert data["tasks"][0]["Nome"] == "Bruno"