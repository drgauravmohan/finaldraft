from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from base.models import (
    Service, ServiceFeature, ServiceDoctor, ServiceTeam,
    Treatment, Ailment, Technology, ServiceAccordion, SuccessStory
)
import requests
from io import BytesIO


class Command(BaseCommand):
    help = 'Populate database with sample services (Cardiology, Angioplasty, ECG)'

    def download_image(self, url):
        """Download image from URL and return ContentFile"""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return ContentFile(response.content)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Failed to download image from {url}: {e}'))
        return None

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate services...')

        # Clear existing data
        self.stdout.write('Clearing existing services...')
        Service.objects.all().delete()

        # Create Cardiology Service
        self.create_cardiology_service()

        # Create Angioplasty Service
        self.create_angioplasty_service()

        # Create ECG Service
        self.create_ecg_service()

        self.stdout.write(self.style.SUCCESS('Successfully populated all services!'))

    def create_cardiology_service(self):
        self.stdout.write('Creating Cardiology service...')

        # Note: For images, we'll use placeholder URLs since we can't upload actual files via command
        # In production, you should upload images through Django admin
        service = Service.objects.create(
            name='Cardiology',
            slug='cardiology',
            meta_title='Best Cardiology Hospital | Expert Heart Care Services',
            meta_description='Leading cardiology department offering comprehensive heart care with world-class cardiologists, advanced diagnostics, and minimally invasive treatments.',
            meta_keywords='cardiology, heart care, cardiac services, best cardiologist',
            overview_title='Comprehensive Heart Care',
            is_active=True
        )

        # Features
        features_data = [
            'State-of-the-art cardiac catheterization labs',
            'Advanced heart failure management program',
            '24/7 emergency cardiac care services',
            'Comprehensive preventive cardiology programs',
            'Expert team of interventional cardiologists',
            'Cutting-edge cardiac imaging technology',
        ]
        for idx, feature in enumerate(features_data):
            ServiceFeature.objects.create(service=service, title=feature, order=idx)

        # Doctor
        ServiceDoctor.objects.create(
            service=service,
            name='Dr. Rajesh Kumar',
            title='Chairman, Department of Cardiology',
            message='At our cardiology department, we believe in providing patient-centered care with the latest advancements in cardiovascular medicine. Our team is dedicated to delivering personalized treatment plans that address each patient\'s unique needs, combining clinical excellence with compassionate care.',
            order=1
        )

        # Teams
        teams_data = [
            ('Expert Cardiologists', '', 'Our team comprises highly skilled cardiologists with decades of combined experience in treating complex cardiac conditions. From routine check-ups to advanced interventions, we provide comprehensive care at every stage.'),
            ('Advanced Cardiac Imaging', '', 'We utilize state-of-the-art imaging technologies including 3D echocardiography, cardiac MRI, and CT angiography to accurately diagnose and monitor heart conditions, enabling precise treatment planning.'),
            ('Interventional Cardiology', '', 'Our interventional cardiology team specializes in minimally invasive procedures, offering patients faster recovery times and excellent outcomes through techniques like angioplasty, stenting, and valve repairs.'),
        ]
        for idx, (title, subtitle, desc) in enumerate(teams_data):
            ServiceTeam.objects.create(
                service=service, title=title, subtitle=subtitle,
                description=desc, order=idx
            )

        # Treatments
        treatments_data = [
            ('Coronary Angioplasty', 'A minimally invasive procedure to open blocked coronary arteries using a balloon catheter, often combined with stent placement. This procedure restores blood flow to the heart muscle and is performed with high precision by our expert team.'),
            ('Pacemaker Implantation', 'Advanced cardiac device implantation for patients with irregular heart rhythms. Our electrophysiologists use the latest technology to ensure optimal device placement and programming for each patient\'s specific needs.'),
            ('Heart Valve Repair', 'Comprehensive valve repair and replacement procedures including minimally invasive approaches. We offer both surgical and transcatheter options, tailoring the treatment to each patient\'s condition and overall health.'),
            ('Cardiac Ablation', 'Catheter-based procedure to treat arrhythmias by creating controlled lesions in heart tissue. Our electrophysiology team uses advanced 3D mapping systems for precise targeting and successful outcomes.'),
        ]
        for idx, (name, desc) in enumerate(treatments_data):
            Treatment.objects.create(
                service=service, name=name, description=desc, order=idx
            )

        # Ailments
        ailments_data = [
            ('Coronary Artery Disease', 'Comprehensive diagnosis and treatment of blocked or narrowed coronary arteries causing chest pain, shortness of breath, and heart attacks. We offer medical management, lifestyle counseling, and interventional procedures.'),
            ('Heart Failure', 'Advanced management of heart failure through medications, device therapy, and lifestyle modifications. Our heart failure team provides comprehensive care including monitoring, medication optimization, and cardiac rehabilitation.'),
            ('Arrhythmias', 'Expert treatment of irregular heart rhythms including atrial fibrillation, ventricular tachycardia, and other rhythm disorders. We offer medication management, cardioversion, ablation, and device implantation.'),
            ('Valvular Heart Disease', 'Complete evaluation and treatment of heart valve disorders including stenosis and regurgitation. Our team offers both medical management and surgical interventions including minimally invasive valve repairs.'),
        ]
        for idx, (name, desc) in enumerate(ailments_data):
            Ailment.objects.create(
                service=service, name=name, description=desc, order=idx
            )

        # Technologies
        technologies_data = [
            ('3D Echocardiography', 'Advanced three-dimensional imaging technology providing detailed visualization of heart structures and function. This enables more accurate diagnosis of complex cardiac conditions and better treatment planning.'),
            ('Cardiac CT & MRI', 'State-of-the-art computed tomography and magnetic resonance imaging systems offering non-invasive assessment of cardiac anatomy, function, and blood flow with exceptional detail and accuracy.'),
            ('Intravascular Ultrasound (IVUS)', 'Real-time ultrasound imaging from inside blood vessels during interventional procedures. This technology allows precise assessment of vessel dimensions and plaque characteristics for optimal stent placement.'),
            ('Electrophysiology Mapping', 'Advanced 3D cardiac mapping systems that create detailed electrical maps of the heart, enabling precise identification and treatment of arrhythmia sources through targeted ablation procedures.'),
        ]
        for idx, (name, desc) in enumerate(technologies_data):
            Technology.objects.create(
                service=service, name=name, short_description=desc, order=idx
            )

        # Accordions (Sub-specializations)
        subspecializations_data = [
            ('Interventional Cardiology', 'Our interventional cardiology division specializes in catheter-based treatments for cardiovascular diseases. Using minimally invasive techniques, we perform complex procedures including angioplasty, stenting, valve repairs, and structural heart interventions with excellent outcomes and faster recovery times.'),
            ('Electrophysiology', 'The electrophysiology unit focuses on diagnosing and treating heart rhythm disorders. Our team performs advanced procedures including ablation therapy, pacemaker and defibrillator implantations, and cardiac resynchronization therapy using cutting-edge mapping and ablation technologies.'),
            ('Heart Failure & Transplant', 'Specialized care for patients with advanced heart failure, including medical optimization, mechanical circulatory support, and heart transplant evaluation. Our multidisciplinary team provides comprehensive management from early stages to advanced therapies.'),
            ('Preventive Cardiology', 'Focus on preventing cardiovascular disease through risk assessment, lifestyle modification, and medical management. We offer comprehensive screening programs, lipid management, and personalized prevention strategies for optimal heart health.'),
        ]
        for idx, (title, desc) in enumerate(subspecializations_data):
            ServiceAccordion.objects.create(
                service=service, section_type='subspecialization',
                title=title, description=desc, order=idx
            )

        self.stdout.write(self.style.SUCCESS('Cardiology service created!'))

    def create_angioplasty_service(self):
        self.stdout.write('Creating Angioplasty service...')

        service = Service.objects.create(
            name='Angioplasty & Stenting',
            slug='angioplasty',
            meta_title='Advanced Angioplasty Procedures | Coronary Stenting Experts',
            meta_description='Expert angioplasty and stenting procedures by leading interventional cardiologists using latest technology for optimal patient outcomes.',
            meta_keywords='angioplasty, coronary stenting, PCI, interventional cardiology',
            overview_title='Advanced Coronary Interventions',
            is_active=True
        )

        # Features
        features_data = [
            'Advanced coronary intervention expertise',
            'Latest drug-eluting stent technology',
            'Minimally invasive radial artery approach',
            '24/7 primary angioplasty for heart attacks',
            'Complex lesion intervention capabilities',
            'High success rates with minimal complications',
        ]
        for idx, feature in enumerate(features_data):
            ServiceFeature.objects.create(service=service, title=feature, order=idx)

        # Doctor
        ServiceDoctor.objects.create(
            service=service,
            name='Dr. Anil Sharma',
            title='Director, Interventional Cardiology',
            message='Angioplasty has revolutionized the treatment of coronary artery disease. Our team performs hundreds of successful procedures annually using the latest techniques and technology. We specialize in complex cases including chronic total occlusions and multi-vessel disease, always prioritizing patient safety and optimal outcomes.',
            order=1
        )

        # Teams
        teams_data = [
            ('Expert Interventional Team', '', 'Our interventional cardiologists are trained at the world\'s leading institutions and bring extensive experience in performing complex angioplasty procedures. We handle everything from routine cases to the most challenging interventions with equal expertise.'),
            ('State-of-the-Art Cath Labs', '', 'We operate multiple advanced catheterization laboratories equipped with latest imaging technology including IVUS, OCT, and FFR. These tools enable precise assessment and treatment of coronary blockages with optimal results.'),
            ('Rapid Response Team', '', 'Our 24/7 emergency angioplasty team ensures immediate treatment for heart attack patients. With door-to-balloon times among the best in the country, we maximize heart muscle preservation and improve patient outcomes.'),
        ]
        for idx, (title, subtitle, desc) in enumerate(teams_data):
            ServiceTeam.objects.create(
                service=service, title=title, subtitle=subtitle,
                description=desc, order=idx
            )

        # Treatments
        treatments_data = [
            ('Primary Angioplasty', 'Emergency angioplasty performed during acute heart attacks to immediately restore blood flow. Our rapid response protocol ensures minimal delay from hospital arrival to artery opening, maximizing heart muscle preservation and survival rates.'),
            ('Elective Angioplasty', 'Planned angioplasty procedures for stable coronary artery disease. We perform thorough evaluation including stress testing and advanced imaging to determine optimal timing and approach for each patient\'s specific anatomy and condition.'),
            ('Complex Coronary Interventions', 'Specialized procedures for challenging cases including chronic total occlusions, left main disease, and bifurcation lesions. Our team uses advanced techniques and technologies to successfully treat cases other centers may decline.'),
            ('Drug-Eluting Stent Implantation', 'Placement of latest generation drug-eluting stents that release medication to prevent re-narrowing. These advanced stents provide excellent long-term results with reduced need for repeat procedures compared to older technologies.'),
        ]
        for idx, (name, desc) in enumerate(treatments_data):
            Treatment.objects.create(
                service=service, name=name, description=desc, order=idx
            )

        # Ailments
        ailments_data = [
            ('Acute Myocardial Infarction', 'Immediate treatment of heart attacks through emergency angioplasty. Our rapid response team works around the clock to provide life-saving intervention within optimal timeframes, significantly improving survival and recovery outcomes.'),
            ('Stable Angina', 'Management of chest pain due to coronary blockages through angioplasty and stenting. We carefully evaluate each patient to determine the best timing and approach, balancing symptom relief with procedural risks.'),
            ('Unstable Angina', 'Urgent treatment of worsening chest pain indicating high-risk coronary disease. Our team performs timely angioplasty to prevent heart attacks and stabilize patients, often using advanced imaging to guide optimal treatment strategies.'),
            ('Chronic Total Occlusion', 'Specialized intervention for completely blocked coronary arteries, often long-standing. Our experts use advanced techniques including retrograde approaches and specialized equipment to successfully open these challenging blockages.'),
        ]
        for idx, (name, desc) in enumerate(ailments_data):
            Ailment.objects.create(
                service=service, name=name, description=desc, order=idx
            )

        # Technologies
        technologies_data = [
            ('Intravascular Ultrasound (IVUS)', 'Real-time ultrasound imaging from inside coronary arteries provides detailed assessment of plaque characteristics and vessel dimensions. This ensures optimal stent sizing and placement for best long-term results.'),
            ('Optical Coherence Tomography (OCT)', 'High-resolution optical imaging technology offering microscopic visualization of coronary artery walls. OCT helps assess stent deployment, detect edge dissections, and evaluate complex lesions with unprecedented detail.'),
            ('Fractional Flow Reserve (FFR)', 'Physiological assessment of coronary blockages to determine which lesions require treatment. FFR measurements guide decision-making, ensuring we treat only significant blockages while avoiding unnecessary stenting.'),
            ('Rotational Atherectomy', 'Advanced device for treating heavily calcified coronary lesions that cannot be adequately dilated with balloons alone. This technology enables successful stent delivery in complex anatomies previously considered unsuitable.'),
        ]
        for idx, (name, desc) in enumerate(technologies_data):
            Technology.objects.create(
                service=service, name=name, short_description=desc, order=idx
            )

        # Accordions (Sub-specializations)
        subspecializations_data = [
            ('Primary PCI for STEMI', 'Specialized 24/7 program for emergency angioplasty in ST-elevation heart attacks. Our dedicated team ensures rapid response with door-to-balloon times consistently meeting international guidelines, maximizing patient survival and heart function preservation.'),
            ('Complex Coronary Intervention', 'Expert handling of challenging cases including chronic total occlusions, bifurcation lesions, left main disease, and multi-vessel interventions. We use advanced techniques and specialized equipment unavailable at most centers.'),
            ('Radial Artery Approach', 'Preferred access through the wrist rather than groin, offering increased patient comfort, faster mobilization, and reduced bleeding complications. Our team has extensive experience with radial procedures including complex cases.'),
            ('Hemodynamic Support', 'Advanced mechanical circulatory support during high-risk procedures using devices like Impella or intra-aortic balloon pumps. This enables safe treatment of patients with severe heart dysfunction who require revascularization.'),
        ]
        for idx, (title, desc) in enumerate(subspecializations_data):
            ServiceAccordion.objects.create(
                service=service, section_type='subspecialization',
                title=title, description=desc, order=idx
            )

        self.stdout.write(self.style.SUCCESS('Angioplasty service created!'))

    def create_ecg_service(self):
        self.stdout.write('Creating ECG service...')

        service = Service.objects.create(
            name='ECG & Cardiac Diagnostics',
            slug='ecg',
            meta_title='Advanced ECG Testing | Comprehensive Cardiac Diagnostics',
            meta_description='State-of-the-art ECG and cardiac diagnostic services including stress testing, Holter monitoring, and advanced electrophysiology studies.',
            meta_keywords='ECG, electrocardiogram, cardiac testing, heart diagnostics',
            overview_title='Comprehensive Cardiac Diagnostics',
            is_active=True
        )

        # Features
        features_data = [
            'Advanced 12-lead ECG with AI interpretation',
            'Exercise and pharmacological stress testing',
            'Holter and event monitoring services',
            'Signal-averaged ECG for arrhythmia risk',
            'Same-day reporting and consultation',
            'Mobile cardiac telemetry capabilities',
        ]
        for idx, feature in enumerate(features_data):
            ServiceFeature.objects.create(service=service, title=feature, order=idx)

        # Doctor
        ServiceDoctor.objects.create(
            service=service,
            name='Dr. Priya Mehta',
            title='Head, Cardiac Diagnostics & Electrophysiology',
            message='Accurate cardiac diagnosis is the foundation of effective treatment. Our diagnostic services combine cutting-edge technology with expert interpretation to provide precise assessment of heart function and rhythm. From basic ECGs to advanced electrophysiology studies, we offer comprehensive testing tailored to each patient\'s needs.',
            order=1
        )

        # Teams
        teams_data = [
            ('Expert Diagnostic Team', '', 'Our team includes cardiologists specialized in non-invasive cardiac testing and electrophysiology. Every test is carefully performed and interpreted by experienced physicians who understand the nuances of cardiac diagnostics.'),
            ('Advanced Technology', '', 'We utilize the latest ECG and monitoring equipment with digital storage and AI-assisted interpretation. Our systems detect subtle abnormalities that might be missed with older technology, ensuring accurate diagnosis.'),
            ('Rapid Turnaround', '', 'Understanding the importance of timely diagnosis, we provide same-day results for most tests with immediate physician review for urgent cases. Critical findings are communicated immediately to referring physicians.'),
        ]
        for idx, (title, subtitle, desc) in enumerate(teams_data):
            ServiceTeam.objects.create(
                service=service, title=title, subtitle=subtitle,
                description=desc, order=idx
            )

        # Treatments/Services
        treatments_data = [
            ('12-Lead ECG', 'Standard electrocardiogram recording heart electrical activity from 12 different angles. This fundamental test detects arrhythmias, heart attacks, chamber enlargement, and many other cardiac conditions within minutes.'),
            ('Exercise Stress Testing', 'ECG monitoring during treadmill or bicycle exercise to assess heart response to physical stress. This test evaluates exercise capacity, detects exercise-induced arrhythmias, and identifies coronary artery disease.'),
            ('Holter Monitoring', '24 to 48-hour continuous ECG recording capturing heart rhythm during normal daily activities. Essential for detecting intermittent arrhythmias, assessing pacemaker function, and evaluating symptoms like palpitations or dizziness.'),
            ('Event Monitoring', 'Extended cardiac monitoring (up to 30 days) that records ECG when patients activate the device during symptoms. Ideal for infrequent symptoms that might be missed during shorter monitoring periods.'),
        ]
        for idx, (name, desc) in enumerate(treatments_data):
            Treatment.objects.create(
                service=service, name=name, description=desc, order=idx
            )

        # Conditions Diagnosed
        ailments_data = [
            ('Arrhythmias', 'Comprehensive evaluation of irregular heart rhythms including atrial fibrillation, premature beats, and dangerous ventricular arrhythmias. Our extended monitoring options ensure accurate diagnosis even for intermittent rhythm disturbances.'),
            ('Myocardial Ischemia', 'Detection of reduced blood flow to heart muscle through stress testing and advanced ECG analysis. Early identification enables timely treatment to prevent heart attacks and preserve heart function.'),
            ('Conduction Disorders', 'Diagnosis of electrical pathway problems including heart blocks and bundle branch blocks. Accurate assessment helps determine need for pacemaker therapy or other interventions to maintain proper heart rhythm.'),
            ('Cardiac Structural Abnormalities', 'ECG signs of chamber enlargement, ventricular hypertrophy, and other structural changes. These findings guide further testing and management of underlying conditions like hypertension or valve disease.'),
        ]
        for idx, (name, desc) in enumerate(ailments_data):
            Ailment.objects.create(
                service=service, name=name, description=desc, order=idx
            )

        # Technologies
        technologies_data = [
            ('AI-Enhanced ECG Analysis', 'Artificial intelligence algorithms analyze ECG patterns to detect subtle abnormalities and predict future cardiac events. This technology augments physician interpretation, improving diagnostic accuracy and early detection of heart disease.'),
            ('Digital Holter Systems', 'Advanced portable recorders with Bluetooth connectivity and real-time data transmission. These comfortable, lightweight devices provide high-quality recordings with sophisticated analysis software for comprehensive rhythm assessment.'),
            ('Wireless Telemetry', 'Real-time cardiac monitoring for inpatients with immediate alert systems for dangerous rhythms. Our telemetry unit uses advanced algorithms to minimize false alarms while ensuring rapid response to true emergencies.'),
            ('Signal-Averaged ECG', 'Specialized technique detecting microscopic electrical disturbances (late potentials) that predict risk of dangerous ventricular arrhythmias. Important for risk stratification in patients with heart disease or unexplained syncope.'),
        ]
        for idx, (name, desc) in enumerate(technologies_data):
            Technology.objects.create(
                service=service, name=name, short_description=desc, order=idx
            )

        # Accordions (Sub-specializations)
        subspecializations_data = [
            ('Arrhythmia Diagnostics', 'Comprehensive evaluation of heart rhythm disorders using ECG, Holter monitoring, event recorders, and electrophysiology studies. We identify arrhythmia type, frequency, and clinical significance to guide appropriate treatment strategies.'),
            ('Exercise Physiology', 'Expert stress testing services including treadmill, bicycle, and pharmacological stress tests. Our exercise physiologists and cardiologists provide safe, effective testing with immediate interpretation and risk assessment.'),
            ('Ambulatory Monitoring', 'Extended cardiac rhythm monitoring programs using various technologies from 24-hour Holter to 30-day event recorders and implantable loop recorders. We match monitoring duration and technology to clinical needs.'),
            ('Pediatric ECG Services', 'Specialized cardiac diagnostics for children including age-appropriate exercise protocols and pediatric ECG interpretation. Our team understands normal pediatric variants and pathological findings requiring intervention.'),
        ]
        for idx, (title, desc) in enumerate(subspecializations_data):
            ServiceAccordion.objects.create(
                service=service, section_type='subspecialization',
                title=title, description=desc, order=idx
            )

        self.stdout.write(self.style.SUCCESS('ECG service created!'))
