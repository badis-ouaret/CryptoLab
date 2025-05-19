from Model.exceptions import *
import math



class CalculMatriciel():
        
    @staticmethod
    def initialiseMat(lin,col):
        if lin >=1 and col >=1:        
            return [[0] * col for _ in range(lin)]
        else:
            return None
    
    @staticmethod
    def pgcd(num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

        
    @staticmethod
    def isMat(liste):
        if not isinstance(liste, list) or not liste:  # Vérifie que c'est une liste non vide
            return False
    
        longueur_premiere_ligne = len(liste[0])  # Longueur de la première ligne

        for ligne in liste:
            if not isinstance(ligne, list) or len(ligne) != longueur_premiere_ligne:
                return False  # Une ligne n'est pas une liste ou a une longueur différente

        return True
    @staticmethod
    def dimentionsMat(mat):
        if not CalculMatriciel.isMat(mat):
            
            raise WrongMatFormatException()
        col = 0
        lin = 0
        if mat :
            col = len(mat[0])
            lin = len(mat)     
        
        return lin,col
    
    @staticmethod
    def dimentionColMat(mat):
        if not CalculMatriciel.isMat(mat):
            raise WrongMatFormatException()
        col = 0
        if mat :
            col =len(mat[0])
        
        return col
    @staticmethod
    def dimentionLinMat(mat):
        if not CalculMatriciel.isMat(mat):
            raise WrongMatFormatException()
        
        lin = 0
        if mat :
            lin =len(mat)
        
        return lin        

    @staticmethod
    def produitMatriciel(mat1,mat2):
        if not CalculMatriciel.isMat(mat1) and CalculMatriciel.isMat(mat2):
            raise WrongMatFormatException()
        
        if CalculMatriciel.dimentionColMat(mat1) != CalculMatriciel.dimentionLinMat(mat2):
            raise ProduitMatImpossibleException()
        
        (mat1Lin,mat1Col) = CalculMatriciel.dimentionsMat(mat1)
        (mat2Lin,mat2Col) = CalculMatriciel.dimentionsMat(mat2)
        
        matRes = CalculMatriciel.initialiseMat(mat1Lin,mat2Col)
        
        for k in range(mat2Col):
            for i in range(mat1Lin):
                prod = 0
                for j in range(mat1Col):
                    
                    prod += mat1[i][j]*mat2[j][k]
                matRes[i][k] = prod
        
        return matRes       
    
    @staticmethod
    def produitMatNum(mat,num):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        M = CalculMatriciel.initialiseMat(matLin,matCol)
        for i in range(matLin):
            for j in range(matCol):
                M[i][j] = mat[i][j]*num
        return M
    @staticmethod
    def modMatNum(mat,num):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        M = CalculMatriciel.initialiseMat(matLin,matCol)
        for i in range(matLin):
            for j in range(matCol):
                M[i][j] = mat[i][j] % num
        return M
    @staticmethod
    def matIsInversible(mat):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        if not matLin == matCol:
            return False
        return CalculMatriciel.detMat(mat) !=0
    
    @staticmethod
    def matIsInversibleModNum(mat,num):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        if not matLin == matCol:
            return False
        det = CalculMatriciel.detMat(mat)
        
        return det !=0 and  CalculMatriciel.numInversibleModNum(det,num)
    
    @staticmethod
    def numInversibleModNum(num1,num2):        
        return CalculMatriciel.pgcd(int(num1),int(num2)) == 1
    
    @staticmethod
    def numInversModNum(num1,num2):
        if not CalculMatriciel.numInversibleModNum(num1,num2):
            raise NumNonInversibleModNumException(num1," n'est pas inversible modulo ",num2)
        n = num1%num2
        res = 1
        while (n * res) % num2 != 1 and res < num2:
            res +=1
        if res < 26:
            return res
        else:
            return None
        

    @staticmethod
    def matIsCarree(mat):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        return matLin == matCol
    
    @staticmethod
    def sousMat(mat ,lin,col):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        M = CalculMatriciel.initialiseMat(matLin-1,matCol-1)
        k = 0 
        g = 0
        for i in range(matLin):            
            for j in range(matCol):
                if i !=lin and j!=col:
                    M[k][g] = mat[i][j]
                    g +=1
                    if g == matCol-1:
                        g=0
                        k+=1
        
        return M
        
        
    @staticmethod   
    def detMat(mat):
        if not CalculMatriciel.matIsCarree(mat) : 
            raise WrongMatFormatException("Impossible de calculer le determinant d'une matrice non carree")
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        if matLin == 1 and matCol == 1:
            return mat[0][0]
        
        elif matLin == 2 and matCol == 2:
            return (mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1])
        else:
            det = 0
            lin = 0
            for col in range(matCol):
                det = det + ((-1)**(lin+col))*mat[lin][col]*CalculMatriciel.detMat(CalculMatriciel.sousMat(mat,lin,col))
            return det
    
    
    
    @staticmethod
    def comatriceMat(mat):
        if CalculMatriciel.matIsCarree(mat):
            matLin,matCol = CalculMatriciel.dimentionsMat(mat)
            M = CalculMatriciel.initialiseMat(matLin,matCol)
            for i in range(matLin):
                for j in range(matCol):
                    
                    detComa = CalculMatriciel.detMat(CalculMatriciel.sousMat(mat,i,j))
                    M[i][j] = ((-1)**(i+j))*detComa
                         
            return M
        else:
            return None #transformer en exception et la gerer  comme il se doit
    
    
    @staticmethod
    def transposeeMat(mat):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        transpo = CalculMatriciel.initialiseMat(matCol,matLin)
        for i in range(matLin):
            for j in range(matCol):
                transpo[j][i] = mat[i][j]
        
        return transpo
    
    
    @staticmethod
    def calculMatInvers(mat):
        if not CalculMatriciel.matIsInversible(mat):
            raise WrongMatFormatException("La matrice n'est pas invesible !")
        detMat = CalculMatriciel.detMat(mat)
        # Définir la précision (par exemple, 100 chiffres significatifs)
        #mpmath.mp.dps = 100
        # Nombre à inverser
        #x = mpmath.mpf(float(detMat))
        # Calcul de l'inverse
        #inverse_x = 1 / x    
        inverse_x = 1/detMat   
        comatrice = CalculMatriciel.comatriceMat(mat)
        transpoComat = CalculMatriciel.transposeeMat(comatrice)        
        return CalculMatriciel.produitMatNum(transpoComat,(inverse_x))
    
    @staticmethod
    def calculMatInversModNum(mat,num):
        if not CalculMatriciel.matIsInversibleModNum(mat,num):
            raise WrongMatFormatException("La matrice n'est pas invesible mod ",num,".")
        detMat = CalculMatriciel.detMat(mat)
        inversDetMatModNum = CalculMatriciel.numInversModNum(detMat,num)  
        comatrice = CalculMatriciel.comatriceMat(mat)
        transpoComat = CalculMatriciel.transposeeMat(comatrice)
        transpoComat = CalculMatriciel.modMatNum(transpoComat,num)
        temp = CalculMatriciel.produitMatNum(transpoComat,(inversDetMatModNum))     
        return CalculMatriciel.modMatNum(temp,num)
    
    def addValToMat(mat,val):
        matLin,matCol = CalculMatriciel.dimentionsMat(mat)
        M = mat
        for i in range(matLin):
            for j in range(matCol):
                M[i][j] += val
        return M
    
    
    
# def main():

#     # Matrices de test (dimensions > 2)
#     mat3x4 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#     mat4x3 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
#     mat3x3_A = np.array([[2,0,0], [0,3,0], [0,0,4]])  # det = 24
#     mat3x3_B = np.array([[5,1,2], [0,3,4], [1,0,6]])   # det = 5*(3*6 - 4*0) - 1*(0*6 -4*1) + 2*(0*0 -3*1) = 90 - (-4) + (-6) = 88
#     mat4x4 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
#     mat3x3_sing = np.array([[1,2,3], [4,5,6], [7,8,9]])  # det = 0 (lignes colinéaires)

#     print("=== Test des méthodes de dimensions ===")
#     try:
#         # Test 1.1: Matrice 3x4
#         assert CalculMatriciel.dimentionsMat(mat3x4) == (3, 4)
#         assert CalculMatriciel.dimentionLinMat(mat3x4) == 3
#         assert CalculMatriciel.dimentionColMat(mat3x4) == 4
#         print("Test 1.1 Réussi")
#     except AssertionError:
#         print("Test 1.1 Échec")

#     try:
#         # Test 1.2: Input non-numpy (3x3)
#         CalculMatriciel.dimentionsMat([[1,2,3], [4,5,6], [7,8,9]])
#         print("Test 1.2 Échec: Exception non levée")
#     except WrongMatFormatException:
#         print("Test 1.2 Réussi")

#     print("\n=== Test produit matriciel ===")
#     try:
#         # Test 2.1: Produit 3x3 * 3x3
#         mat1 = np.array([[2,0,1], [3,1,4], [5,2,1]])
#         mat2 = np.array([[1,3,2], [2,4,1], [0,5,3]])
#         resultat = CalculMatriciel.produitMatriciel(mat1, mat2)
#         attendu = np.array([[2*1+0*2+1*0, 2*3+0*4+1*5, 2*2+0*1+1*3],
#                             [3*1+1*2+4*0, 3*3+1*4+4*5, 3*2+1*1+4*3],
#                             [5*1+2*2+1*0, 5*3+2*4+1*5, 5*2+2*1+1*3]])
#         assert np.array_equal(resultat, attendu)
#         print("Test 2.1 Réussi")
#     except AssertionError:
#         print("Test 2.1 Échec")

#     try:
#         # Test 2.2: Produit impossible (3x4 * 3x3)
#         CalculMatriciel.produitMatriciel(mat3x4, mat3x3_A)
#         print("Test 2.2 Échec: Exception non levée")
#     except ProduitMatImpossibleException:
#         print("Test 2.2 Réussi")

#     print("\n=== Test produit par scalaire ===")
#     try:
#         resultat = CalculMatriciel.produitMatNum(mat3x3_A, 3)
#         attendu = np.array([[6,0,0], [0,9,0], [0,0,12]])
#         assert np.array_equal(resultat, attendu)
#         print("Test 3 Réussi")
#     except AssertionError:
#         print("Test 3 Échec")

#     print("\n=== Test modulo ===")
#     try:
#         mat = np.array([[7,8,9], [10,11,12], [13,14,15]])
#         resultat = CalculMatriciel.modMatNum(mat, 5)
#         attendu = np.array([[2,3,4], [0,1,2], [3,4,0]])
#         assert np.array_equal(resultat, attendu)
#         print("Test 4 Réussi")
#     except AssertionError:
#         print("Test 4 Échec")

#     print("\n=== Test inversibilité ===")
#     try:
#         assert not CalculMatriciel.matIsInversible(mat3x4)  # Non carrée
#         assert not CalculMatriciel.matIsInversible(mat3x3_sing)  # det=0
#         assert CalculMatriciel.matIsInversible(mat3x3_B)  # det=88 ≠0
#         print("Test 5 Réussi")
#     except AssertionError:
#         print("Test 5 Échec")

#     print("\n=== Test sous-matrice ===")
#     try:
#         # Sous-matrice de mat4x4 en (0,0)
#         sous_mat = CalculMatriciel.sousMat(mat4x4, 0, 0)
#         attendu = np.array([[6,7,8], [10,11,12], [14,15,16]])
#         assert np.array_equal(sous_mat, attendu)
#         print("Test 6 Réussi")
#     except AssertionError:
#         print("Test 6 Échec")

#     print("\n=== Test déterminant ===")
#     try:
#         assert CalculMatriciel.detMat(mat3x3_A) == 24
#         assert CalculMatriciel.detMat(mat3x3_B) == 88
#         print("Test 7 Réussi")
#     except AssertionError:
#         print("Test 7 Échec")

#     print("\n=== Test comatrice ===")
#     try:
#         # Comatrice de mat3x3_A (diagonale)
#         comatrice = CalculMatriciel.comatriceMat(mat3x3_A)
#         attendu = np.array([[12, 0, 0], [0, 8, 0], [0, 0, 6]])  # Mineurs avec signes
#         assert np.array_equal(comatrice, attendu)
#         print("Test 8 Réussi")
#     except AssertionError:
#         print("Test 8 Échec")

#     print("\n=== Test transposée ===")
#     try:
#         transpo = CalculMatriciel.transposeeMat(mat3x4)
#         attendu = np.array([[1,5,9], [2,6,10], [3,7,11], [4,8,12]])
#         assert np.array_equal(transpo, attendu)
#         print("Test 9 Réussi")
#     except AssertionError:
#         print("Test 9 Échec")

#     print("\n=== Test inversion matricielle ===")
#     try:
#         inverse = CalculMatriciel.calculMatInvers(mat3x3_A)
#         produit = CalculMatriciel.produitMatriciel(mat3x3_A,inverse)
#         #produit = np.dot(mat3x3_A, inverse)
#         print(produit)        
#         print("Test 10 Réussi")
#     except AssertionError as e:
#         print(f"Test 10 Échec: {e}")
#     except WrongMatFormatException:
#         print("Test 10 Échec: Exception incorrecte")

# def main():

#     # Création des matrices de test
#     mat2x2 = np.array([[1, 2], [3, 4]])
#     mat2x3 = np.array([[1, 2, 3], [4, 5, 6]])
#     mat3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     mat_inversible = np.array([[4, 7], [2, 6]])  # det = 4*6 - 7*2 = 24 - 14 = 10

#     # Début des tests
#     print("=== Test des méthodes de dimensions ===")
#     try:
#         # Test 1: Dimensions d'une matrice 2x3
#         assert CalculMatriciel.dimentionsMat(mat2x3) == (2, 3)
#         assert CalculMatriciel.dimentionLinMat(mat2x3) == 2
#         assert CalculMatriciel.dimentionColMat(mat2x3) == 3
#         print("Test 1.1 Réussi")
#     except AssertionError as e:
#         print(f"Test 1.1 Échec: {e}")

#     try:
#         # Test 1.2: Input non numpy
#         CalculMatriciel.dimentionsMat([[1, 2], [3, 4]])
#         print("Test 1.2 Échec: L'exception n'a pas été levée")
#     except WrongMatFormatException:
#         print("Test 1.2 Réussi")

#     print("\n=== Test du produit matriciel ===")
#     try:
#         # Test 2.1: Produit valide
#         mat1 = np.array([[1, 2], [3, 4]])
#         mat2 = np.array([[5, 6], [7, 8]])
#         resultat = CalculMatriciel.produitMatriciel(mat1, mat2)
#         attendu = np.array([[19, 22], [43, 50]])
#         assert np.array_equal(resultat, attendu)
#         print("Test 2.1 Réussi")
#     except AssertionError:
#         print("Test 2.1 Échec: Résultat incorrect")

#     try:
#         # Test 2.2: Dimensions incompatibles
#         mat1 = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
#         mat2 = np.array([[1, 2], [3, 4]])         # 2x2
#         CalculMatriciel.produitMatriciel(mat1, mat2)
#         print("Test 2.2 Échec: Exception non levée")
#     except ProduitMatImpossibleException:
#         print("Test 2.2 Réussi")

#     print("\n=== Test du produit par un scalaire ===")
#     try:
#         resultat = CalculMatriciel.produitMatNum(mat2x2, 2)
#         attendu = np.array([[2, 4], [6, 8]])
#         assert np.array_equal(resultat, attendu)
#         print("Test 3 Réussi")
#     except AssertionError:
#         print("Test 3 Échec")

#     print("\n=== Test du modulo ===")
#     try:
#         mat = np.array([[7, 8], [9, 10]])
#         resultat = CalculMatriciel.modMatNum(mat, 3)
#         attendu = np.array([[1, 2], [0, 1]])
#         assert np.array_equal(resultat, attendu)
#         print("Test 4 Réussi")
#     except AssertionError:
#         print("Test 4 Échec")

#     print("\n=== Test d'inversibilité ===")
#     try:
#         # Matrice non carrée
#         assert not CalculMatriciel.matIsInversible(mat2x3)
#         # Matrice singulière
#         mat_singuliere = np.array([[1, 2], [2, 4]])
#         assert not CalculMatriciel.matIsInversible(mat_singuliere)
#         # Matrice inversible
#         assert CalculMatriciel.matIsInversible(mat_inversible)
#         print("Test 5 Réussi")
#     except AssertionError:
#         print("Test 5 Échec")

#     print("\n=== Test sous-matrice ===")
#     try:
#         sous_mat = CalculMatriciel.sousMat(mat3x3, 0, 0)
#         attendu = np.array([[5, 6], [8, 9]])
#         assert np.array_equal(sous_mat, attendu)
#         print("Test 6 Réussi")
#     except AssertionError:
#         print("Test 6 Échec")

#     print("\n=== Test déterminant ===")
#     try:
#         assert CalculMatriciel.detMat(mat2x2) == -2
#         assert CalculMatriciel.detMat(mat_inversible) == 10
#         print("Test 7 Réussi")
#     except AssertionError:
#         print("Test 7 Échec")

#     print("\n=== Test comatrice ===")
#     try:
#         comatrice = CalculMatriciel.comatriceMat(mat2x2)
#         attendu = np.array([[4, -3], [-2, 1]])
#         assert np.array_equal(comatrice, attendu)
        
#         print("Test 8 Réussi")
#     except AssertionError:
#         print("Test 8 Échec")

#     print("\n=== Test transposée ===")
#     try:
#         transpo = CalculMatriciel.transposeeMat(mat2x3)
#         attendu = np.array([[1, 4], [2, 5], [3, 6]])
#         assert np.array_equal(transpo, attendu)
#         print("Test 9 Réussi")
#     except AssertionError:
#         print("Test 9 Échec")

#     print("\n=== Test inversion matricielle ===")
#     try:
#         inverse = CalculMatriciel.calculMatInvers(mat_inversible)
#         produit = np.dot(mat_inversible, inverse)
#         # Vérifier si le produit est proche de l'identité (à cause des float)
#         assert np.allclose(produit, np.eye(2))
#         print("Test 10 Réussi")
#     except AssertionError:
#         print("Test 10 Échec")
#     except WrongMatFormatException:
#         print("Test 10 Échec: Exception levée incorrectement")
# if __name__ == "__main__":
#      main()
