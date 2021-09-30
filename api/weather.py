from datetime import datetime, timedelta
import requests

def getCWB(datail):
##################################################
#                                                #
#               Get data from CWB                #
#                                                #
##################################################
    def getData(datail:str, params = {}):
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/'
        with open('data/CWBparams.json', 'r', encoding='utf-8') as defaultParams:
            params.update(eval(defaultParams.read()))
        response = requests.get(url + datail, params = params).json()
        return response['records'] if 'records' in response.keys() else None
##################################################
#                                                #
#                  Process data                  #
#                                                #
##################################################
    def F_C0032_001(raw):  # 一般天氣預報-今明 36 小時天氣預報
        data = {'title': raw['datasetDescription'], 'dataset': []}
        for i in [0, 1, 2]:
            dataset = {}
            for str in ['startTime', 'endTime']:
                date = raw['location'][0]['weatherElement'][0]['time'][i][str]
                dataset[str] = '{}/{} {}時'.format(date[5:7], date[8:10], date[11:13])
            dataset['location'] = []
            for rawLocation in raw['location']:
                location = {'location': rawLocation['locationName'], 'element': {}}
                for element in rawLocation['weatherElement']:
                    location['element'][element['elementName']] = element['time'][i]['parameter']['parameterName']
                dataset['location'].append(location)
            data['dataset'].append(dataset)
        return data
    
    
    def __earthquakeReporter(raw):
        data = {'time': '', 'content': '', 'title': raw['datasetDescription']}
        raw = raw['earthquake'][0]
        time = datetime.fromisoformat(raw['earthquakeInfo']['originTime'])
        data['time'] = time.isoformat()
        data['content'] = time.strftime('%m/%d %H:%M') + raw['reportContent'][11:]
        data['image'] = raw['reportImageURI']
        data['footer'] = {
            'text': raw['reportRemark'],
            'icon_url': 'https://www.cwb.gov.tw/V8/assets/img/win10/cwbPinlogo.png'
        }
        data['field'] = [
            {'name': '資料來源', 'value': '[中央氣象局]({})'.format(raw['web'])},
            {'name': '地震編號', 'value': raw['earthquakeNo'] if raw['earthquakeNo'] % 1000 else '小區域有感地震'},
            {'name': '發生時間', 'value': time.strftime('%Y 年 %m 月 %d 日\n%H 時 %M 分 %S 秒')},
            {'name': '震源深度', 'value': ' '.join(map(lambda t: str(raw['earthquakeInfo']['depth'][t]), ['value', 'unit'])),},
            {'name': '地震規模', 'value': ' '.join(map(lambda t: str(raw['earthquakeInfo']['magnitude'][t]), ['magnitdueType', 'magnitudeValue']))},
            {'name': '震央位置', 'value': '北緯 {epi[epiCenterLat][value]} 度・東經 {epi[epiCenterLon][value]} 度\n{epi[location]}'.format(epi = raw['earthquakeInfo']['epiCenter']).replace(' (', '\n(').replace('  ', ' ')}
        ]
        for area in sorted(raw['intensity']['shakingArea'], key = lambda x: x['areaDesc'], reverse = True):
            if '最' in area['areaDesc']:
                data['field'].append({'name' : area['areaDesc'], 'value' : area['areaName'], 'inline': False})
        return data
    def E_A0015_001(raw):   # 顯著有感地震報告
        return __earthquakeReporter(raw)
    def E_A0016_001(raw):   # 小區域有感地震報告
        return __earthquakeReporter(raw)
    
    
    def W_C0033_002(raw):   # 天氣警特報
        if not raw['record']:
            return None
        datas = []
        for record in raw['record']:
            data = {
                'time': '',
                'title': record['datasetInfo']['datasetDescription'],
                'description': record['contents']['content']['contentText'].strip()
            }
            time = datetime.fromisoformat(record['datasetInfo']['validTime']['startTime'])
            data['time'] = time.isoformat()
            data['timestamp'] = time - timedelta(hours = 8)
            data['footer'] = {
                'text': "以上資料由 交通部中央氣象局 提供",
                'icon_url': 'https://www.cwb.gov.tw/V8/assets/img/win10/cwbPinlogo.png'
            }
            data['field'] = [
                {'name': '發布時間', 'value': time.strftime('%Y 年 %m 月 %d 日 %H 時 %M 分')},
                {'name': '資料來源', 'value': '[中央氣象局](https://www.cwb.gov.tw/V8/C/P/Warning/FIFOWS.html)'}
            ]
            if 'hazardConditions' in record.keys():
                data['field'].insert(0, {
                    'inline': False,
                    'name': '影響範圍',
                    'value': '、'.join(map(lambda x: x['locationName'], record['hazardConditions']['hazards']['hazard']['info']['affectedAreas']['location']))
                })
            datas.append(data)
        return sorted(datas, key = lambda x: x['time'], reverse = True)[0]
    
    
    raw = getData(datail)
    if not raw:
        return None
    return eval(datail.replace('-', '_') + '(raw)')