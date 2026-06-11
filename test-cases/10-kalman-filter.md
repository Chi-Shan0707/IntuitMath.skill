# Test Case: Kalman Filter Motivation

**Question**: "Why can a Kalman filter turn noisy observations into stable estimates?"

## Expected Pattern

This case checks whether IntuitMath can explain an applied mathematical
algorithm as a repair to a concrete inference problem. The answer should avoid
starting with matrix recursions. It should first show the tension between a
model prediction and a noisy measurement.

1. **MOTIVATION**: A moving object has hidden state; sensors are noisy; neither
   prediction nor observation is trustworthy alone.
2. **TOOLKIT RECONSTRUCTION**: Deterministic simulation ignores measurement
   correction; raw measurements ignore dynamics; averaging ignores changing
   state.
3. **PRE-RIGOROUS**: Keep two things at every step: a best guess and uncertainty
   about that guess.
4. **BOLD ATTEMPT**: Blend prediction and measurement by a weight. The weight
   should be high when the sensor is reliable and low when the prediction is
   reliable.
5. **RIGOROUS REPAIR**: Under linear-Gaussian assumptions, the optimal weight is
   the Kalman gain, obtained from covariance propagation and Bayesian updating.
6. **SKEPTIC PASS**: State what breaks when noise is non-Gaussian, dynamics are
   nonlinear, or the model covariance is misspecified.
7. **REFLECTION ANCHOR**: Ask whether the filter is "smoothing data" or
   maintaining a belief state.

## Key Elements to Check

- [ ] Begins from hidden state plus noisy sensor, not from formulas.
- [ ] Includes a one-dimensional toy example such as tracking position.
- [ ] Explains prediction step and update step in words before equations.
- [ ] Interprets covariance as uncertainty, not just a matrix variable.
- [ ] Interprets Kalman gain as trust allocation between model and observation.
- [ ] Gives the linear-Gaussian equations after the intuition.
- [ ] Names at least one failure mode or extension: EKF, UKF, particle filter,
      bad covariance tuning, nonlinear dynamics, outliers.
- [ ] Ends with a reflection question.

## Example Output (Abbreviated)

> **The problem.** Imagine tracking a cart on a line. The motion model says
> where it should be after one second, but friction and bumps make the prediction
> imperfect. The sensor gives a position reading, but the reading jitters. If
> you trust only the model, errors drift. If you trust only the sensor, the
> estimate jitters.
>
> **The hidden variable.** The real state might be position and velocity,
> \(x_t = [p_t, v_t]^T\). We do not observe \(x_t\) directly. We observe
> \(z_t = Hx_t + \text{noise}\).
>
> **The bold attempt.** First predict:
> \[
> \hat x_{t|t-1} = A\hat x_{t-1|t-1}.
> \]
> Then compare the sensor reading with what the prediction expected to see:
> \[
> y_t = z_t - H\hat x_{t|t-1}.
> \]
> The innovation \(y_t\) is the surprise. If the surprise comes from a reliable
> sensor, correct a lot. If it comes from a noisy sensor, correct only a little.
>
> **Kalman's repair.** The filter carries both a mean estimate and covariance.
> Prediction increases or transports uncertainty:
> \[
> P_{t|t-1} = AP_{t-1|t-1}A^T + Q.
> \]
> Updating chooses the gain
> \[
> K_t = P_{t|t-1}H^T(HP_{t|t-1}H^T + R)^{-1}.
> \]
> This is not an arbitrary smoothing knob. It is the trust ratio implied by the
> predicted uncertainty and sensor noise.
>
> **Caution.** The classical filter is exactly optimal in the linear-Gaussian
> setting. With nonlinear dynamics or heavy-tailed outliers, the same equations
> can become overconfident. That is why extended, unscented, and particle
> filters exist.
>
> **Something to sit with.** Is a Kalman filter mainly a denoising algorithm, or
> is it a compact way to update belief under uncertainty?
