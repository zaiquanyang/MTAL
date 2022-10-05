import os, sys, torch, pickle, h5py
import numpy as np

# path = '/data/code/ZSL_Code/MTAL/data/CUB/feature_map_ResNet_101_CUB.hdf5'
# hf = h5py.File(path, 'r')

# features = np.array(hf.get('feature_map'))
# labels = np.array(hf.get('labels'))
# trainval_loc = np.array(hf.get('trainval_loc'))
# test_seen_loc = np.array(hf.get('test_seen_loc'))
# test_unseen_loc = np.array(hf.get('test_unseen_loc'))
# att = np.array(hf.get('att'))
# original_att = np.array(hf.get('original_att'))
# w2v_att = np.array(hf.get('w2v_att'))

# data_dict  = {}

# data_dict['features'] = features
# data_dict['labels'] = labels
# data_dict['trainval_loc'] = trainval_loc
# data_dict['test_seen_loc'] = test_seen_loc
# data_dict['test_unseen_loc'] = test_unseen_loc
# data_dict['att'] = att
# data_dict['original_att'] = original_att
# data_dict['w2v_att'] = w2v_att

# data_file = open('/data/code/ZSL_Code/MTAL/data/CUB/feature_map_ResNet_101_CUB.pickle', 'wb')
# pickle.dump(data_dict, data_file)
# data_file.close()

data_file = open('/data/code/ZSL_Code/MTAL/data/CUB/feature_map_ResNet_101_CUB.pickle', 'rb')
data = pickle.load(data_file)
data_file.close()

# features = np.array(hf.get('feature_map'))
#         # features.shape 11788 x 2048x 14 x 14
#         # shape = features.shape
#         # features = features.reshape(shape[0],shape[1],shape[2]*shape[3])
#         # pdb.set_trace()
#         labels = np.array(hf.get('labels'))
#         trainval_loc = np.array(hf.get('trainval_loc'))
#         # train_loc = np.array(hf.get('train_loc')) #--> train_feature = TRAIN SEEN
#         # val_unseen_loc = np.array(hf.get('val_unseen_loc')) #--> test_unseen_feature = TEST UNSEEN
#         test_seen_loc = np.array(hf.get('test_seen_loc'))
#         test_unseen_loc = np.array(hf.get('test_unseen_loc'))
        
#         if self.is_unsupervised_attr:
#             print('Unsupervised Attr')
#             class_path = './w2v/{}_class.pkl'.format(self.dataset)
#             with open(class_path,'rb') as f:
#                 w2v_class = pickle.load(f)
#             temp = np.array(hf.get('att'))
#             print(w2v_class.shape,temp.shape)
#             # assert w2v_class.shape == temp.shape
#             w2v_class = torch.tensor(w2v_class).float()
            
#             U, s, V = torch.svd(w2v_class)
#             reconstruct = torch.mm(torch.mm(U,torch.diag(s)),torch.transpose(V,1,0))
#             print('sanity check: {}'.format(torch.norm(reconstruct-w2v_class).item()))
            
#             print('shape U:{} V:{}'.format(U.size(),V.size()))
#             print('s: {}'.format(s))
            
#             self.w2v_att = torch.transpose(V,1,0).to(self.device)
#             self.att = torch.mm(U,torch.diag(s)).to(self.device)
#             self.normalize_att = torch.mm(U,torch.diag(s)).to(self.device)
            
#         else:
#             print('Expert Attr')
#             att = np.array(hf.get('att'))
#             self.att = torch.from_numpy(att).float().to(self.device)
            
#             original_att = np.array(hf.get('original_att'))
#             self.original_att = torch.from_numpy(original_att).float().to(self.device)
            
#             w2v_att = np.array(hf.get('w2v_att'))
#             self.w2v_att = torch.from_numpy(w2v_att).float().to(self.device)
            
#             self.normalize_att = self.original_att/100
