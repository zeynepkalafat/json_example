
import json
import numpy as np

TEST_SIZES = [95, 90, 70]

results = {
    '95': {
        'svm': {
            'linear': {
                'acc': []
            }

        }
    },
    '90': {
        'svm': {
            'linear': {
                'acc': []
            }

        }
    },
    '70': {
        'svm': {
            'linear': {
                'acc': []
            }
        }
    },
}

for i in range(1000):
    if i%2 ==0:
        results['95']['svm']['linear']['acc'].append(i)
    if i%3 == 0:
        results['90']['svm']['linear']['acc'].append(i)
    if i % 5 == 0:
        results['70']['svm']['linear']['acc'].append(i)


results['95']['svm']['linear']['acc'] = np.mean( results['95']['svm']['linear']['acc'])
results['90']['svm']['linear']['acc'] = np.mean( results['90']['svm']['linear']['acc'])
results['70']['svm']['linear']['acc'] = np.mean( results['70']['svm']['linear']['acc'])

results_str = json.dumps(results, sort_keys=True, indent=4)
f = open('deneme.json', 'w')
f.write(results_str)
f.close()