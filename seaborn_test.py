# go to anaconda2/scripts & run conda install jupyter or ipython if not installed
# run jupyter notebook which will open dashboard. click on new python2 notebook on right top corner
#http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python2
# paste below code 

%matplotlib inline

#shift + enter 

#paste below code 
import seaborn as sns 
# Load one of the data sets that come with seaborn
tips = sns.load_dataset("tips")

sns.jointplot("total_bill", "tip", tips, kind='reg');

#You should see plots in browser


#reads
#http://jupyter-notebook.readthedocs.io/en/latest/notebook.html#opening-notebooks
#http://twiecki.github.io/blog/2014/11/18/python-for-data-science/

