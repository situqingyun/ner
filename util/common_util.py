'''
    LAK：lake，湖泊
    RES：水库
    ORG：机构
    LOC：地区
    TER：水利术语
    PER：人员
    DAM：大坝
    HYD：水电站
    RIV：河流
    OTH：其它

    training data's length: 4919
    testing data's length: 628
'''
labels = ['LAK', 'RES', 'ORG', 'LOC', 'TER', 'PER', 'DAM', 'HYD', 'RIV', 'OTH']
label_dict = {'RIV': 6340, 'LAK': 1293, 'LOC': 6638, 'TER': 1567, 'RES': 629, 'OTH': 51, 'HYD': 169, 'DAM': 107, 'ORG': 284, 'PER': 81}

def find_all(s, sub):
    index_list = []
    index = s.find(sub)
    while index != -1:
        index_list.append(index)
        index = s.find(sub, index + 1)

    if len(index_list) > 0:
        return index_list
    else:
        return -1

train_file = 'data/bmes_train.json'
test_file = 'data/bmes_test.json'

test_result_file = 'result/test_result.json'