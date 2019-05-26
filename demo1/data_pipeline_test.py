def test_pipeline():
    data_pipeline = Pipeline()

    test_arrays = []
    for i in range(4):
        test_arrays.append(np.loadtxt(f'test_data_{i}.csv', delimiter=','))

    processed_arrays = data_pipeline.process(test_arrays)

    results = []
    for i in range(4):
        results.append(np.loadtxt(f'results_{i}.csv', delimiter=','))

    for proc_arr,result in zip(processed_arrays, results):
        assert proc_arr == result

