import numpy as np
import matplotlib.pyplot as plt

#codigo para reproduzir a distribuicao de energis do artigo

n_pon = 500000  #numero de pontos

mew = 1000   #[MeV] peak
sigma = 250  #[MeV] width
sigma_e = 275  #dois parametros de ajuste
mean_e = 0     #á funcao de distribuicao de energia dos eletroes

eletroes_x = np.random.normal(0, 1/np.sqrt(2) , n_pon)  #coordenada x dos eletroes
eletroes_y = np.random.normal(0, 1/np.sqrt(2) , n_pon)  #coordenada y dos eletroes

energia_e = sigma_e*np.sqrt(2*np.log((sigma_e * np.sqrt(2 * np.pi)) * np.sqrt(eletroes_y**2 + eletroes_x**2))) + mean_e #distribuicao da energia dos eletroes

Energia = [100 + i/n_pon*(mew + sigma/3) for i in range(n_pon)]  #pontos de energia

Energia = np.array(Energia)

dN_dE = 32*(mew + sigma/3 - Energia)**(-3/2) * np.exp(-sigma/(2*(mew + sigma/3 - Energia)))  #expressao analitica da distribuicao de energia

n, bins, patches = plt.hist(energia_e, 100, density=True, facecolor='b', alpha=0.75)  #histograma da distribuicao de energias dos eletroes

plt.plot(Energia, dN_dE)   #grafico da expressao analitica para a distribuicao de energia dos eletroes

plt.show()

