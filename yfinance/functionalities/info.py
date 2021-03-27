def info_func(data):  
    info = {}
    items = ['summaryProfile', 'summaryDetail', 'quoteType',
              'defaultKeyStatistics', 'assetProfile', 'summaryDetail', 'financialData']
    for item in items:
        if isinstance(data.get(item), dict):
            info.update(data[item])

    info['regularMarketPrice'] = info['regularMarketOpen']
    info['logo_url'] = ""
    try:
        domain = info['website'].split('://')[1].split('/')[0].replace('www.', '')
        info['logo_url'] = 'https://logo.clearbit.com/%s' % domain
    except Exception:
        pass
    
    return info
