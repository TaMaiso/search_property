class MockGetFilter():
    def get_filter(self):
        return "WHERE sh.status_id = 3 OR sh.status_id = 4 OR sh.status_id = 5"