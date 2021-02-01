import json
from util.common_util import *

train_file_processed = 'data/processed/bmes_train.csv'

def prepare_data():

    # print(json.load(open(train_file, 'r')))
    train_data = json.load(open(train_file, 'r'))
    test_data = json.load(open(test_file, 'r'))
    entities_dict = dict()
    for i in train_data:
        entities = i.get('entities', [])
        for e in entities:
            label = e.split('-')[1]
            entities_dict[label] = entities_dict.get(label, 0)+1
            # entities_set.add(e.split('-')[1])
    print(entities_dict)
    print('training data\'s length: {}'.format(len(train_data)))
    print('testing data\'s length: {}'.format(len(test_data)))

def label_data():
    train_data = json.load(open(train_file, 'r'))
    # test_data = json.load(open(test_file, 'r'))

    texts=[]
    results = []

    for i in train_data:
        entities = i.get('entities', [])
        text = i.get('text', '')
        texts.append(list(text))
        # labels_indices = dict()
        result = ['OTH']*len(text)
        for e in entities:
            es = e.split('-')
            entity = es[0]
            label = es[1]
            start_indices = find_all(text, entity)
            for idx in start_indices:
                result[idx]='B-'+label
                if len(entity)>1:
                    for d in range(idx+1,idx+len(entity)):
                        result[d] = 'I-'+label
        # i['label']=','.join(result)
        results.append(result)

    with open('data/processed/train.txt', 'w') as f:
        for i in range(len(texts)):
            for j in range(len(texts[i])):
                f.write(texts[i][j]+' '+results[i][j]+'\n')
            f.write('\n')

def label_test_data():
    train_data = json.load(open(test_file, 'r'))
    # test_data = json.load(open(test_file, 'r'))

    texts=[]
    results = []

    for i in train_data:
        # entities = i.get('entities', [])
        text = i.get('text', '')
        texts.append(list(text))
        # labels_indices = dict()
        result = ['OTH']*len(text)
        results.append(result)

    with open('data/processed/test.txt', 'w') as f:
        for i in range(len(texts)):
            for j in range(len(texts[i])):
                f.write(texts[i][j]+' '+results[i][j]+'\n')
            f.write('\n')
    print('finished!')

if __name__=='__main__':
    # prepare_data()
    # label_data()
    label_test_data()
