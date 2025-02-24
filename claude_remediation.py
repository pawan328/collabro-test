import subprocess
import json
import logging

class ContainerRemediator:
    def __init__(self, image_name):
        self.image_name = image_name
        self.logger = logging.getLogger(__name__)

    def scan_with_trivy(self):
        """Scan image using Trivy"""
        try:
            result = subprocess.run(['trivy', 'image', '-f', 'json', self.image_name], 
                                    capture_output=True, text=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Trivy scan failed: {e}")
            return None

    def apply_copa_patch(self, vulnerability_report):
        """Apply patches using Copa"""
        try:
            with open('vulnerability_report.json', 'w') as f:
                json.dump(vulnerability_report, f)
            
            result = subprocess.run(['copa', 'patch', '-r', 'vulnerability_report.json', '-i', self.image_name],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                self.logger.info("Successfully applied Copa patches")
                return True
            else:
                self.logger.error(f"Copa patching failed: {result.stderr}")
                return False
        except Exception as e:
            self.logger.error(f"Copa patching failed: {e}")
            return False

    def remediate(self):
        """Main remediation workflow"""
        try:
            # Scan with Trivy
            scan_results = self.scan_with_trivy()
            if not scan_results:
                return False

            # Apply patches using Copa
            if self.apply_copa_patch(scan_results):
                self.logger.info("Vulnerabilities patched successfully")
                return True
            else:
                self.logger.warning("Vulnerability patching failed")
                return False

        except Exception as e:
            self.logger.error(f"Remediation process failed: {e}")
            return False

if __name__ == "__main__":
    remediator = ContainerRemediator("app-java-container:latest")
    remediator.remediate()
