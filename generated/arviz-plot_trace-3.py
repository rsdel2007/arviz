lines = (('theta_t',{'theta_t_dim_0':0}, [-1]),)
coords = {'theta_t_dim_0': [0, 1], 'school':['Lawrenceville']}
az.plot_trace(data, var_names=('theta_t', 'theta'), coords=coords, lines=lines)