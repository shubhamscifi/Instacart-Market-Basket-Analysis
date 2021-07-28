# Submissions will be evaluated based on their Samples Mean F1-Score.(each order is a sample.)
# https://scikit-learn.org/stable/modules/model_evaluation.html#:~:text=F%CE%B2(y%2Cy%5E)-,%22samples%22,-1%7CS%7C%E2%88%91s
# https://www.kaggle.com/c/instacart-market-basket-analysis/discussion/33357#:~:text=You%20take%20the%20average%20of%20all%20the%20F1%20scores%20across%20the%20order_ids

def f_score_helper(df,target):
    '''
    Returns pd.Series of f1-score, precision and recall for given order_id.
    '''
    TP = df['reordered'] @ df[target] # true positive(numerator)
    den_pr = df[target].sum() # denominator for precision
    den_re = df['reordered'].sum()  # denominator for recall
    if (den_pr==0 and den_re==0):
        # if both the actual and prediction is None.
        TP+=1
    if den_pr==0:
        # if prediction is None.
        den_pr+=1
    if den_re==0:
        # if actual is None.
        den_re+=1
    
    return pd.Series({'f_score':2*TP/(den_re+den_pr),
                      'precision' :TP/(den_pr),
                      'recall': TP/(den_re)})

def f_score(dataset,target='reordered',pr_re=False):
    '''
    Returns Samples F1-score.

    pr_re : if True return (f-score, precision & recall) otherwise only f-score.
    '''
    f_score,pr,re = dataset[['order_id','reordered',target]]\
                    .groupby('order_id')\
                    .apply(f_score_helper,target)\
                    .mean()
    
    if (pr_re==True):
        return f_score,pr,re
    return f_score
