#Tech-Gym-13-11-A
#�f�B�[�v���[�j���O�摜���ފ�:CNN
#�菑�������f�[�^
#60,000����28x28�C10�̐����̔����摜��10,000���̃e�X�g�p�摜�f�[�^�Z�b�g

#�K�v�ȃ��C�u����
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline
%config InlineBackend.figure_format = 'retina'

#MNIST�f�[�^
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#�s��̑傫�����m�F
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)     

#�͂��߂�100��\��
plt.figure(figsize=(15, 15))
gs = gridspec.GridSpec(10,10)

for i in range(10):
    for j in range(10):
        plt.axis("off")
        plt.subplot(gs[i,j])
        plt.imshow(X_test[i+j], "gray")
        plt.text(0, 5, y_test[i+j], fontsize=16, color='red')
plt.show()

