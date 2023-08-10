pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'my-repo']],
                    submoduleCfg: [],
                    userRemoteConfigs: [[
                        credentialsId: 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCz/XC+ni3pbCNZjvoMjBiM7bthZjv
                        9hup4h3I6QjeAkYl/6SlxEtS22fQ+LTrbL91IHikJUc1g/0LrM167ixkgCG/mDAWzp9l2u8EMjrCGnh79uDVgwGSZcmMfAbPOVOV3XLhDkZhd+Ei2+
                        1sphAtmbVvSZSHy0vKPXBJsW5xPJ8B0XEcN4en65I2vae0MEhMwXIubHO0noRvtQhKaAn9TJh4N6H0uPnetNuJaAlXWiY10xdHEUfBt7+NlYOkN2dMe
                        bspkI3c2XZ71KHqbbpAiOfw66qm2eptWQpZzfNK0oszQNQzD4ovtAzDz4A+O4y5mbKtZU/ytJHyivqHFrkP5pQR0Dn4qvx3BvBmOJe67ZDSvQ5KJ9QI/2
                        k+LaIJ4efKfEdrUuSx2N48RRaI1uaLI6PmakIdsBZ2KMZE5PfDHEfp9ZkZb/PK0IROzUtBOWRnTbH//EBIttbRG5bEJd/rVOgO7013nsILjkoR4ikgQCqxFVMy/
                        JFMA89EeL0D+2rE= dimatsy@Air-Dima
', // Используйте ID учетных данных SSH, который вы создали
                        url: 'https://github.com/TsykalanovDima/Jen' // SSH URL вашего репозитория на GitHub
                    ]]
                ])
            }
        }
    }
}
