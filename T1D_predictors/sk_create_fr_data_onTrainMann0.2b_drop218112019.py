import numpy as np
import pandas as pd
from tsfresh import extract_features, select_features
from  tsfresh.feature_selection.relevance import calculate_relevance_table

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn import linear_model

from sklearn.model_selection import GridSearchCV
from tsfresh.transformers import  FeatureSelector






eQTL_table = pd.read_table('/nesi/project/uoa02723/Mann_sklearn/Mann_on_training/std80_Denis_total_Gwas_cat_Denis_2017_all_combined_eQTL_table02042019.txt')
x_features = eQTL_table[eQTL_table.columns[6:]]
y_phenotype = eQTL_table['PHENOTYPE'] - 1

select = FeatureSelector(fdr_level=0.2)
select.fit(x_features,y_phenotype)
#X_selected0_1 = select_features(x_features, y_phenotype,test_for_binary_target_real_feature='mann', test_for_real_target_binary_feature='mann', fdr_level=0.2 )

#full_columns = list(eQTL_table.columns[:6]) + list( X_selected0_1.columns)
#selected_std_full = eQTL_table[full_columns]


eQTL_table100 = pd.read_table('/nesi/project/uoa02723/Mann_sklearn/Mann_on_training/std_Denis_total_Gwas_cat_Denis_2017_all_combined_eQTL_table02042019.txt')
#eQTL_table100_selected = eQTL_table100[selected_std_full.columns]

eQTL_table100_selected = eQTL_table100

y_train = eQTL_table100_selected['PHENOTYPE'] - 1
x_train = eQTL_table100_selected[eQTL_table100_selected.columns[6:]]

#X = x_train
X = select.transform(x_train)
Y = y_train


parameters = {'C':[1],'max_iter':[500],'l1_ratio':[1]}
lg_clf = LogisticRegression(random_state=1, solver='saga',n_jobs=-1, penalty='elasticnet' )
grid_clf = GridSearchCV(lg_clf, parameters, scoring='roc_auc', n_jobs=-1,iid=False, cv=5)
X1 = X
X_drop = X1.drop(columns=['Lung--rs6679677_A--AP4B1-AS1'])
grid_clf.fit(X_drop,Y)

f= open("/nesi/project/uoa02723/Mann_sklearn/Mann_on_training/results_final/full_lg_saga_c1l1max500_dropLung--rs6679677_A--AP4B1-AS1.txt","w+")

f.write('full_lg_saga_c1l1max500_dropLung--rs6679677_A--AP4B1-AS1\n')
f.write('5 fold:\n')
f.write('grid_clf.best_score_: ' + str(grid_clf.best_score_) + '\n')
f.write('grid_clf.best_estimator_: ' + str(grid_clf.best_estimator_) + '\n')
f.write('grid_clf.best_params_: ' + str(grid_clf.best_params_) + '\n')
f.write('grid_clf.scorer_: ' + str(grid_clf.scorer_) + '\n')
f.write('grid_clf.best_score_: ' + str(grid_clf.best_score_) + '\n')
f.write('grid_clf.best_score_: ' + str(grid_clf.best_score_) + '\n')

lg_clf_best_grid = grid_clf.best_estimator_

model_Max = roc_auc_score(Y, lg_clf_best_grid.predict_proba(X_drop)[:,1])

num_coef = np.sum(lg_clf_best_grid.coef_[0,:] != 0)

cv_results = grid_clf.cv_results_
std_cv = cv_results['std_test_score'][grid_clf.best_index_]

f.write('--------------------------------------------------------------------\n\n')
f.write('In-Sample AUC: ' + str(model_Max) + '\n')
f.write('10 fold MeanCV AUC: ' + str(grid_clf.best_score_) + '\n')
f.write('Standard Deviation CV AUC: ' + str(std_cv) + '\n')

f.write('num_coef: ' + str(num_coef) + '\n')
f.write('\n\n\n')



X_header = np.array(X_drop.columns)
best_clf =  grid_clf.best_estimator_
data_array = np.vstack((X_header,best_clf.coef_[0,:]))
model_weights = pd.DataFrame(data=data_array.T,columns=['Data_feature', 'Weight'])
model_weights.to_csv('/nesi/project/uoa02723/Mann_sklearn/Mann_on_training/results_final/full_lg_saga_c1l1max500_dropLung--rs6679677_A--AP4B1-AS1weights.txt', sep='\t',index=False,line_terminator='\n')


#-----------------------------------------------------------------


f.close()



f= open("/nesi/project/uoa02723/Mann_sklearn/Mann_on_training/results_final/full_lg_saga_c1l1max500_dropTestis--rs3087243_A--CTLA4.txt","w+")

#------------------------------------------------------------------------------------------------

parameters = {'C':[1],'max_iter':[500],'l1_ratio':[1]}
lg_clf = LogisticRegression(random_state=1, solver='saga',n_jobs=-1, penalty='elasticnet' )
grid_clf = GridSearchCV(lg_clf, parameters, scoring='roc_auc', n_jobs=-1,iid=False, cv=5)
X1 = X
X_drop = X1.drop(columns=['Testis--rs3087243_A--CTLA4'])
grid_clf.fit(X_drop,Y)


f.write('full_lg_saga_c1l1max500_dropTestis--rs3087243_A--CTLA4\n')
f.write('5 fold:\n')
f.write('grid_clf.best_score_: ' + str(grid_clf.best_score_) + '\n')
f.write('grid_clf.best_estimator_: ' + str(grid_clf.best_estimator_) + '\n')
f.write('grid_clf.best_params_: ' + str(grid_clf.best_params_) + '\n')
f.write('grid_clf.scorer_: ' + str(grid_clf.scorer_) + '\n')
f.write('grid_clf.best_score_: ' + str(grid_clf.best_score_) + '\n')
f.write('grid_clf.best_score_: ' + str(grid_clf.best_score_) + '\n')

lg_clf_best_grid = grid_clf.best_estimator_

model_Max = roc_auc_score(Y, lg_clf_best_grid.predict_proba(X_drop)[:,1])

num_coef = np.sum(lg_clf_best_grid.coef_[0,:] != 0)

cv_results = grid_clf.cv_results_
std_cv = cv_results['std_test_score'][grid_clf.best_index_]

f.write('--------------------------------------------------------------------\n\n')
f.write('In-Sample AUC: ' + str(model_Max) + '\n')
f.write('5 fold MeanCV AUC: ' + str(grid_clf.best_score_) + '\n')
f.write('Standard Deviation CV AUC: ' + str(std_cv) + '\n')

f.write('num_coef: ' + str(num_coef) + '\n')
f.write('\n\n\n')

X_header = np.array(X_drop.columns)
best_clf =  grid_clf.best_estimator_
data_array = np.vstack((X_header,best_clf.coef_[0,:]))
model_weights = pd.DataFrame(data=data_array.T,columns=['Data_feature', 'Weight'])
model_weights.to_csv('/nesi/project/uoa02723/Mann_sklearn/Mann_on_training/results_final/full_lg_saga_c1l1max500_dropTestis--rs3087243_A--CTLA4', sep='\t',index=False,line_terminator='\n')






f.close()



