# 随机森林补全，已弃用

def fill_missing_rf(X,y,to_fill):
    df = X.copy()
    fill = df.loc[:,to_fill]
    df = pd.concat([df.loc[:,df.columns != to_fill],pd.DataFrame(y)],axis=1)
    
    Ytrain = fill[fill.notnull()]
    Ytest = fill[fill.isnull()]
    Xtrain = df.iloc[Ytrain.index,:]
    Xtest = df.iloc[Ytest.index,:]
    
    from sklearn.ensemble import RandomForestRegressor as rfr
    rfr = rfr(n_estimators=40)
    rfr = rfr.fit(Xtrain, Ytrain)
    Ypredict = rfr.predict(Xtest)
    
    return Ypredict

def fill_with_tf(data):
    train_data = data.copy()
    train_data['NumberOfDependents'].fillna(train_data['NumberOfDependents'].median(), inplace=True)

    X = train_data.iloc[:,1:]
    y = train_data['SeriousDlqin2yrs']

    y_pred = fill_missing_rf(X,y,'MonthlyIncome')
    data.loc[data.loc[:,'MonthlyIncome'].isnull(),'MonthlyIncome'] = y_pred