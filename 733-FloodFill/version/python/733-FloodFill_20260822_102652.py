# Last updated: 8/22/2026, 10:26:52 AM
df = visits_no_trans.groupby('customer_id', as_index=False)['visit_id'].count()

return df.rename(columns={'visit_id': 'count_no_trans'})