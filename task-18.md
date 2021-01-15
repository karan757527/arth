
## WordPress Deployment on AWS EC2 and AWS RDS

## Introduction

WordPress is a popular PHP application. It is used over many sites available on the Internet. Our task is to deploy a WordPress website on Amazon EC2 Instance. WordPress needs MySQL Database so we will use Amazon RDS for it.

![](https://cdn-images-1.medium.com/max/3804/0*VnBNP2sdX1VN8Ko5.png)

## Creating MySQL Database with Amazon RDS

 1. Go to Amazon RDS in AWS Console.

 2. Choose MySQL as Database Engine as WordPress uses MySQL Database Engine.

 3. Choose your desired template in the creation wizard (Use free-tier if you want to just test the deployment).

 4. Specify authentication settings like username and password and also give database name.

 5. Next, Choose VPC in which you want to deploy your application.

In this, we created a fully-managed MySQL database using Amazon RDS. Now, we will create an Amazon EC2 instance for running our WordPress site.

![](https://cdn-images-1.medium.com/max/3840/1*uvnHk-CfoUsl8lTwW3M_1g.png)

![](https://cdn-images-1.medium.com/max/3840/1*Hho2liLoPXOtRRLbvV0d2Q.png)

![](https://cdn-images-1.medium.com/max/3840/1*aSu107WMoZHOrTaaG1rhLQ.png)

![](https://cdn-images-1.medium.com/max/3840/1*2bd28Djb7wpGqVd5C95brw.png)

![](https://cdn-images-1.medium.com/max/3840/1*2bd28Djb7wpGqVd5C95brw.png)

![](https://cdn-images-1.medium.com/max/3840/1*g1qhEYaxWBzjwkcibD1acQ.png)

![](https://cdn-images-1.medium.com/max/3840/1*QFyQmsbiboHvgIfy3j_OqA.png)

![](https://cdn-images-1.medium.com/max/3840/1*IDcTMK7_w-ImlBsnQw4wfQ.png)

## Creating an EC2 instance

 1. Choose Machine Image (Prefer Amazon Linux 2 AMI (HVM)).

 2. Choose the desired instance type.

 3. Now, Configure a Security Group allowing SSH from Your IP and HTTP from anywhere.

 4. Get a key pair used for SSH and Launch.

We have successfully launched our EC2 instance. In the next module, we will configure our RDS database to work with our EC2 instance.

![](https://cdn-images-1.medium.com/max/3840/1*MBsoEG8FMWX-cMBOCMp4Jw.png)

![](https://cdn-images-1.medium.com/max/3840/1*9OugcGTuN_lew8VNoIikPg.png)

![](https://cdn-images-1.medium.com/max/3840/1*vffyt_Edb6uLeK5TXXaa9w.png)

![](https://cdn-images-1.medium.com/max/3840/1*4U37HZDX0OyztooWy6zMPA.png)

![](https://cdn-images-1.medium.com/max/3840/1*62pF7RYGcmBTVU8F4HWkyw.png)

![](https://cdn-images-1.medium.com/max/3840/1*2YT1j7V5HH_Ubq4DCQ8o9Q.png)

![](https://cdn-images-1.medium.com/max/3840/1*iQJVNJKp4r-VK0AcHM-VmA.png)

## Configuring RDS Database

 1. Allow EC2 to access RDS by Changing Security Group of RDS.

 2. SSH your EC2 Instance using command *“ssh -i <path/to/pem/file> ec2-user@<publicIpAddress>”.*

 3. Install MySQL on your EC2 Instance by using the command *“sudo yum install -y mysql”.*

 4. Set Environment variable for MySQL host using export *“MYSQL_HOST=<rds-endpoint>”.*

 5. Connect to Database by *“mysql — user=<user> — password=<password> <database-name>”.*

 6. Finally, create a database user for your WordPress application and give it permission to access the database. Run these commands in the terminal, *“CREATE USER ‘<user-name>’ IDENTIFIED BY ‘<password>’;
GRANT ALL PRIVILEGES ON <database-name>.* TO <user-name>;
FLUSH PRIVILEGES;
Exit”.
*Note — This user is different from the user we gave during MySQL Engine Creation.

We learned how to configure network and password security for our RDS database. Our EC2 instance now has network access to our RDS database. Further, we created a database user to be used by your WordPress application.
Now, we will configure our EC2 instance to run the WordPress application.

![](https://cdn-images-1.medium.com/max/3840/1*guSYk8LMw2qAT3xhtY5jEg.png)

![](https://cdn-images-1.medium.com/max/3840/1*rpqN-ivtWwD1phKI1Mdn5w.png)

![](https://cdn-images-1.medium.com/max/3840/1*dMc14lEhMCAY3uSpUHH8IQ.png)

## Configuring WordPress on EC2

 1. Install Apache Web Server on EC2 by using, *“sudo yum install -y httpd”*.

 2. Download and Extract WordPress application by using following commands,
*“wget [https://wordpress.org/latest.tar.gz](https://wordpress.org/latest.tar.gz)
tar -xzf latest.tar.gz”.*

 3. Change into the wordpress directory and create a copy of the default config file using the following commands:
*“cd wordpress
cp wp-config-sample.php wp-config.php”.*

 4. Move WordPress application files into the /var/www/html directory used by Apache using *“sudo cp -r ./* /var/www/html/”*.

 5. Open the wp-config file using *“vim wp-config” *or any other desired editor*.*

 6. Edit the following lines and enter values we got:
*“// ** MySQL settings — You can get this info from your web host ** //
/** The name of the database for WordPress */
define( ‘DB_NAME’, ‘database_name_here’ );
/** MySQL database username */
define( ‘DB_USER’, ‘username_here’ );
/** MySQL database password */
define( ‘DB_PASSWORD’, ‘password_here’ );
/** MySQL hostname */
define( ‘DB_HOST’, ‘localhost’ );”*

 7. Install the WordPress Deployments using, *“sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2”*

 8. Start the service by using the command, *“systemctl start httpd”.*

Now, Click on the Public IP and You must be seeing the WordPress welcome page.

![](https://cdn-images-1.medium.com/max/3840/1*GzK1f9h9rfbs0IzxiohgBQ.png)

![](https://cdn-images-1.medium.com/max/3840/1*0dabChDLDzZHEqvwNHFnJQ.png)

![](https://cdn-images-1.medium.com/max/3840/1*FZPFsp5Cp7IIOzmoGYSRJw.png)

![](https://cdn-images-1.medium.com/max/3840/1*xqubA-M3AmeDDZqEboLA-g.png)

![](https://cdn-images-1.medium.com/max/3840/1*9j72RYA7atshmlvy3wQp5g.png)

![](https://cdn-images-1.medium.com/max/3840/1*fnuhAqRzrWb9LetiS435WA.png)

![](https://cdn-images-1.medium.com/max/3840/1*BpnxjI5Csfdb5ncU6dkaGA.png)

![](https://cdn-images-1.medium.com/max/2400/0*_QYUyZgCzFkK9JRU.jpeg)
