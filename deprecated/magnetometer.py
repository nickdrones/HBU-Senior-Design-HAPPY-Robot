from i2clibraries import i2c_hmc5883l
import time

while(1==1):
        hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
        hmc5883l.setContinuousMode()
        hmc5883l.setDeclination(2, 15)
        print(hmc5883l)
        time.sleep(1)