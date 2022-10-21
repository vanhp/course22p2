# Autogenerated by nbdev

d = { 'settings': { 'branch': 'master',
                'doc_baseurl': '/course22p2',
                'doc_host': 'https://fastai.github.io',
                'git_url': 'https://github.com/fastai/course22p2',
                'lib_path': 'miniai'},
  'syms': { 'miniai.datasets': { 'miniai.datasets.collate_dict': ('datasets.html#collate_dict', 'miniai/datasets.py'),
                                 'miniai.datasets.inplace': ('datasets.html#inplace', 'miniai/datasets.py')},
            'miniai.learner': { 'miniai.learner.Accuracy': ('learner.html#accuracy', 'miniai/learner.py'),
                                'miniai.learner.Accuracy.forward': ('learner.html#accuracy.forward', 'miniai/learner.py'),
                                'miniai.learner.Callback': ('learner.html#callback', 'miniai/learner.py'),
                                'miniai.learner.CancelBatchException': ('learner.html#cancelbatchexception', 'miniai/learner.py'),
                                'miniai.learner.CancelEpochException': ('learner.html#cancelepochexception', 'miniai/learner.py'),
                                'miniai.learner.CancelFitException': ('learner.html#cancelfitexception', 'miniai/learner.py'),
                                'miniai.learner.CudaCB': ('learner.html#cudacb', 'miniai/learner.py'),
                                'miniai.learner.CudaCB.before_batch': ('learner.html#cudacb.before_batch', 'miniai/learner.py'),
                                'miniai.learner.CudaCB.before_fit': ('learner.html#cudacb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.DataLoaders': ('learner.html#dataloaders', 'miniai/learner.py'),
                                'miniai.learner.DataLoaders.__init__': ('learner.html#dataloaders.__init__', 'miniai/learner.py'),
                                'miniai.learner.DataLoaders.from_dd': ('learner.html#dataloaders.from_dd', 'miniai/learner.py'),
                                'miniai.learner.Learner': ('learner.html#learner', 'miniai/learner.py'),
                                'miniai.learner.Learner.__getattr__': ('learner.html#learner.__getattr__', 'miniai/learner.py'),
                                'miniai.learner.Learner.__init__': ('learner.html#learner.__init__', 'miniai/learner.py'),
                                'miniai.learner.Learner._fit': ('learner.html#learner._fit', 'miniai/learner.py'),
                                'miniai.learner.Learner._one_epoch': ('learner.html#learner._one_epoch', 'miniai/learner.py'),
                                'miniai.learner.Learner.calc_stats': ('learner.html#learner.calc_stats', 'miniai/learner.py'),
                                'miniai.learner.Learner.callback': ('learner.html#learner.callback', 'miniai/learner.py'),
                                'miniai.learner.Learner.fit': ('learner.html#learner.fit', 'miniai/learner.py'),
                                'miniai.learner.Learner.one_batch': ('learner.html#learner.one_batch', 'miniai/learner.py'),
                                'miniai.learner.Learner.one_epoch': ('learner.html#learner.one_epoch', 'miniai/learner.py'),
                                'miniai.learner.Loss': ('learner.html#loss', 'miniai/learner.py'),
                                'miniai.learner.Loss.forward': ('learner.html#loss.forward', 'miniai/learner.py'),
                                'miniai.learner.Metric': ('learner.html#metric', 'miniai/learner.py'),
                                'miniai.learner.Metric.__call__': ('learner.html#metric.__call__', 'miniai/learner.py'),
                                'miniai.learner.Metric.__init__': ('learner.html#metric.__init__', 'miniai/learner.py'),
                                'miniai.learner.Metric.add': ('learner.html#metric.add', 'miniai/learner.py'),
                                'miniai.learner.Metric.add_batch': ('learner.html#metric.add_batch', 'miniai/learner.py'),
                                'miniai.learner.Metric.forward': ('learner.html#metric.forward', 'miniai/learner.py'),
                                'miniai.learner.Metric.reset': ('learner.html#metric.reset', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB': ('learner.html#metricscb', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.__init__': ('learner.html#metricscb.__init__', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.after_batch': ('learner.html#metricscb.after_batch', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.after_epoch': ('learner.html#metricscb.after_epoch', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.before_epoch': ('learner.html#metricscb.before_epoch', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.before_fit': ('learner.html#metricscb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.log': ('learner.html#metricscb.log', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB': ('learner.html#progresscb', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB._log': ('learner.html#progresscb._log', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.after_batch': ('learner.html#progresscb.after_batch', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.before_epoch': ('learner.html#progresscb.before_epoch', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.before_fit': ('learner.html#progresscb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.TrainCB': ('learner.html#traincb', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.backward': ('learner.html#traincb.backward', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.get_loss': ('learner.html#traincb.get_loss', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.predict': ('learner.html#traincb.predict', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.step': ('learner.html#traincb.step', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.zero_grad': ('learner.html#traincb.zero_grad', 'miniai/learner.py'),
                                'miniai.learner.TrainingLearner': ('learner.html#traininglearner', 'miniai/learner.py'),
                                'miniai.learner.TrainingLearner.backward': ('learner.html#traininglearner.backward', 'miniai/learner.py'),
                                'miniai.learner.TrainingLearner.get_loss': ('learner.html#traininglearner.get_loss', 'miniai/learner.py'),
                                'miniai.learner.TrainingLearner.predict': ('learner.html#traininglearner.predict', 'miniai/learner.py'),
                                'miniai.learner.TrainingLearner.step': ('learner.html#traininglearner.step', 'miniai/learner.py'),
                                'miniai.learner.TrainingLearner.zero_grad': ('learner.html#traininglearner.zero_grad', 'miniai/learner.py'),
                                'miniai.learner.identity': ('learner.html#identity', 'miniai/learner.py'),
                                'miniai.learner.to_cuda': ('learner.html#to_cuda', 'miniai/learner.py'),
                                'miniai.learner.with_cbs': ('learner.html#with_cbs', 'miniai/learner.py'),
                                'miniai.learner.with_cbs.__call__': ('learner.html#with_cbs.__call__', 'miniai/learner.py'),
                                'miniai.learner.with_cbs.__init__': ('learner.html#with_cbs.__init__', 'miniai/learner.py')}}}