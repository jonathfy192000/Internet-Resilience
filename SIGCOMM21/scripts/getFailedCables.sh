rm ../processedData/submarineCables/*
python3 analyzeNetworkSubmarine-uniform.py
python3 analyzeNetworkSubmarine-nonUniform.py 0.1 0.01 0.001
python3 analyzeNetworkSubmarine-nonUniform.py 1.0 0.1 0.01